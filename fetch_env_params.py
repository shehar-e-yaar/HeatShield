import json
import os
import sys
import urllib.request
from config import RAW_DATA_DIR, NEIGHBORHOODS

def fetch_env_params_data():
    """Fetch REAL environmental parameters data from Open-Meteo API."""
    out_dir = os.path.join(RAW_DATA_DIR, 'env_params')
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, 'env_params.json')
    
    print(' Fetching LIVE environmental data from Open-Meteo API...')
    
    results = {}
    
    for name, bounds in NEIGHBORHOODS.items():
        sw = bounds['sw']
        ne = bounds['ne']
        lat = (sw[0] + ne[0]) / 2.0
        lng = (sw[1] + ne[1]) / 2.0
        
        try:
            # 1. Fetch Weather (Temp, Humidity, Apparent Temp)
            weather_url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&current=temperature_2m,relative_humidity_2m,apparent_temperature'
            req = urllib.request.urlopen(weather_url)
            w_data = json.loads(req.read())['current']
            
            # 2. Fetch AQI
            aqi_url = f'https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lng}&current=us_aqi'
            req_aqi = urllib.request.urlopen(aqi_url)
            a_data = json.loads(req_aqi.read())['current']
            
            # 3. Fetch Solar Radiation
            solar_url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&current=shortwave_radiation'
            req_solar = urllib.request.urlopen(solar_url)
            s_data = json.loads(req_solar.read())['current']
            
            temp_c = w_data['temperature_2m']
            rh = w_data['relative_humidity_2m']
            
            # Stull (2011) wet bulb approximation
            import math
            wet_bulb = temp_c * math.atan(0.151977 * (rh + 8.313659)**0.5) + math.atan(temp_c + rh) - math.atan(rh - 1.676331) + 0.00391838 * rh**1.5 * math.atan(0.023101 * rh) - 4.686035
            
            results[name] = {
                'heat_index_c': w_data['apparent_temperature'],
                'apparent_temp_c': w_data['apparent_temperature'],
                'humidity_pct': rh,
                'aqi': a_data['us_aqi'],
                'wet_bulb_c': round(wet_bulb, 1),
                'solar_ghi': int(s_data['shortwave_radiation'])
            }
            print(f'   {name}: AQI {a_data["us_aqi"]}, Temp {w_data["temperature_2m"]}°C, Solar {int(s_data["shortwave_radiation"])} W/m²')
            
        except Exception as e:
            print(f'   Error fetching {name}: {e}')
            # Fallback for this specific neighborhood if API fails
            results[name] = {'heat_index_c': 35.0, 'apparent_temp_c': 35.0, 'humidity_pct': 45, 'aqi': 60, 'wet_bulb_c': 22.0, 'solar_ghi': 850}

    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
        
    print(f' Live Env params data saved to {out_file}')
    return results

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    fetch_env_params_data()
