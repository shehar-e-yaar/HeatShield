import json
import os
import pandas as pd
from config import RAW_DATA_DIR, PROCESSED_DATA_DIR, NEIGHBORHOODS
from scoring import normalize_to_100

def load_temperature_data():
    """Load temperature data from raw files."""
    temp_file = os.path.join(RAW_DATA_DIR, 'temperature', 'all_neighborhoods.json')
    if os.path.exists(temp_file):
        with open(temp_file) as f:
            return json.load(f)
    print(' No temperature data found. Run fetch_temperature.py first.')
    return None

def load_census_data():
    """Load census data."""
    census_file = os.path.join(RAW_DATA_DIR, 'census', 'population.json')
    if os.path.exists(census_file):
        with open(census_file) as f:
            return json.load(f)
    print(' No census data found. Run fetch_census.py first.')
    return None

def load_tree_cover_data():
    """Load tree cover data."""
    tree_file = os.path.join(RAW_DATA_DIR, 'environment', 'tree_cover.json')
    if os.path.exists(tree_file):
        with open(tree_file) as f:
            return json.load(f)
    print(' No tree cover data found. Run fetch_tree_cover.py first.')
    return None

def load_env_params_data():
    """Load environmental parameters data."""
    env_file = os.path.join(RAW_DATA_DIR, 'env_params', 'env_params.json')
    if os.path.exists(env_file):
        with open(env_file) as f:
            return json.load(f)
    print(' No environmental parameters data found. Run fetch_env_params.py first.')
    return None

def load_satellite_data():
    """Load satellite segmentation data."""
    sat_file = os.path.join(RAW_DATA_DIR, 'satellite', 'satellite.json')
    if os.path.exists(sat_file):
        with open(sat_file) as f:
            return json.load(f)
    print(' No satellite data found. Run fetch_satellite.py first.')
    return None

def extract_avg_temperature(temp_result):
    """Extract average temperature from FortyGuard result.
    
    The heatmap result contains map_data and stats_data.
    Stats typically include min, max, mean temperatures.
    """
    if not temp_result or 'error' in temp_result:
        return None
    
    result = temp_result.get('result', {})
    stats = result.get('stats_data', {})
    
    # Extract from the verified FortyGuard schema
    if isinstance(stats, dict):
        temp_stats = stats.get('temperature_stats', {})
        if 'mean' in temp_stats:
            return float(temp_stats['mean'])
            
    return None

def build_master_dataset(live_mode=False):
    """Build the master dataset joining all sources."""
    os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
    
    temp_data = load_temperature_data() if live_mode else None
    census_data = load_census_data()
    tree_data = load_tree_cover_data()
    env_params_data = load_env_params_data()
    satellite_data = load_satellite_data()
    
    sample_day_night = {
        'Downtown LA': {'day': 35.0, 'night': 24.0},
        'Boyle Heights': {'day': 36.5, 'night': 24.5},
        'Hollywood': {'day': 34.0, 'night': 23.5},
        'Van Nuys': {'day': 40.0, 'night': 25.0},
        'Compton': {'day': 35.5, 'night': 23.8},
        'Santa Monica': {'day': 28.0, 'night': 20.0},
        'Pacoima': {'day': 41.0, 'night': 25.5},
        'Echo Park': {'day': 34.5, 'night': 23.8},
        'South LA': {'day': 36.0, 'night': 24.2},
        'Encino': {'day': 38.0, 'night': 24.5},
    }
    
    rows = []
    for name in NEIGHBORHOODS:
        row = {'neighborhood': name}
        
        # Temperature
        if temp_data and name in temp_data:
            avg_temp = extract_avg_temperature(temp_data[name])
            if avg_temp is not None:
                row['avg_temp_c'] = round(avg_temp, 1)
                row['avg_temp_f'] = round(avg_temp * 9/5 + 32, 1)
            center = temp_data[name].get('center', {})
            row['lat'] = center.get('lat')
            row['lng'] = center.get('lng')
        else:
            # Use neighborhood center from config
            bbox = NEIGHBORHOODS[name]
            row['lat'] = (bbox['sw'][0] + bbox['ne'][0]) / 2
            row['lng'] = (bbox['sw'][1] + bbox['ne'][1]) / 2
        
        # Census
        if census_data and name in census_data:
            row['population'] = census_data[name]['total']
            row['elderly_pct'] = census_data[name].get('elderly_pct', 0)
            row['children_pct'] = census_data[name].get('children_pct', 0)
            row['median_income'] = census_data[name].get('median_income', 0)
        
        # Tree cover
        if tree_data and name in tree_data:
            row['tree_cover_pct'] = tree_data[name]['tree_cover_pct']
            row['pavement_pct'] = tree_data[name]['pavement_pct']
            row['park_area_acres'] = tree_data[name].get('park_area_acres', 0)
            
        # Env Params (Open-Meteo fallback)
        row['data_source'] = 'open-meteo'
        if env_params_data and name in env_params_data:
            row['heat_index_c'] = env_params_data[name].get('heat_index_c')
            row['apparent_temp_c'] = env_params_data[name].get('apparent_temp_c')
            row['humidity_pct'] = env_params_data[name].get('humidity_pct')
            row['aqi'] = env_params_data[name].get('aqi')
            row['wet_bulb_c'] = env_params_data[name].get('wet_bulb_c')
            row['solar_ghi'] = env_params_data[name].get('solar_ghi')

        # Overwrite heat_index_c with FortyGuard heatmap result if available
        if 'avg_temp_c' in row and row['avg_temp_c'] is not None:
            row['heat_index_c'] = row['avg_temp_c']
            row['data_source'] = 'fortyguard_live'
            
        # Satellite Data
        if satellite_data and name in satellite_data:
            row['buildings_pct'] = satellite_data[name].get('buildings_pct', 0)
            row['roads_pct'] = satellite_data[name].get('roads_pct', 0)
            row['vegetation_pct'] = satellite_data[name].get('vegetation_pct', 0)
            row['bare_soil_pct'] = satellite_data[name].get('bare_soil_pct', 0)
            row['water_pct'] = satellite_data[name].get('water_pct', 0)
            row['impervious_pct'] = row['buildings_pct'] + row['roads_pct']
            
        # Day / Night temps
        if name in sample_day_night:
            row['day_temp_c'] = sample_day_night[name]['day']
            row['day_temp_f'] = round(sample_day_night[name]['day'] * 9/5 + 32, 1)
            row['night_temp_c'] = sample_day_night[name]['night']
            row['night_temp_f'] = round(sample_day_night[name]['night'] * 9/5 + 32, 1)
        
        rows.append(row)
    
    df = pd.DataFrame(rows)
    
    if 'night_temp_c' in df.columns:
        df['night_heat_score'] = normalize_to_100(df['night_temp_c'])
    
    # Save
    output_path = os.path.join(PROCESSED_DATA_DIR, 'master_dataset_la.csv')
    df.to_csv(output_path, index=False)
    print(f'\n Master dataset saved to {output_path}')
    print(f'   {len(df)} neighborhoods, {len(df.columns)} columns')
    print(f'\nColumns: {list(df.columns)}')
    print(f'\n{df.to_string()}')
    return df

if __name__ == '__main__':
    build_master_dataset()
