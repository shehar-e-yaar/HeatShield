import json
import os
from datetime import datetime
from fortyguard_client import FortyGuardClient
from grid_utils import get_neighborhood_polygons
from config import RAW_DATA_DIR

def fetch_all_neighborhoods(date=None, filter_type=3, granularity=100):
    """Fetch heatmap data for all Los Angeles neighborhoods.
    
    Args:
        date: Date to query (YYYY-MM-DD format). Defaults to today.
        filter_type: 3 = single day (safest, uses least credits)
        granularity: 100 = highest resolution
    """
    if date is None:
        # FortyGuard processing lag means today's data is often unavailable (n_cells = 0).
        # We offset by 1 day to ensure we get fully processed thermal data.
        from datetime import timedelta
        date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        
    client = FortyGuardClient()
    polygons = get_neighborhood_polygons()
    results = {}
    
    output_dir = os.path.join(RAW_DATA_DIR, 'temperature')
    os.makedirs(output_dir, exist_ok=True)
    
    combined_file = os.path.join(output_dir, 'all_neighborhoods.json')
    if os.path.exists(combined_file):
        import time
        file_age = time.time() - os.path.getmtime(combined_file)
        if file_age < 3600:
            print("  Using cached temperature data (less than 1 hour old).")
            with open(combined_file, 'r') as f:
                return json.load(f)
    
    print(f'\n  Fetching temperature data for {len(polygons)} neighborhoods...')
    print(f'    Date: {date}, Filter: {filter_type}, Granularity: {granularity}\n')
    
    for i, (name, polygon_data) in enumerate(polygons.items(), 1):
        print(f'[{i}/{len(polygons)}] {name}...')
        try:
            activity_id = client.submit_heatmap(
                polygon_coords=polygon_data['coords'],
                start_date=date,
                filter_type=filter_type,
                granularity=granularity
            )
            result = client.poll_status(activity_id)
            results[name] = {
                'activity_id': activity_id,
                'center': {'lat': polygon_data['center_lat'], 'lng': polygon_data['center_lng']},
                'result': result.get('result', {})
            }
            
            # Save individual result
            safe_name = name.replace(' ', '_').lower()
            with open(os.path.join(output_dir, f'{safe_name}.json'), 'w') as f:
                json.dump(results[name], f, indent=2)
            
            print(f'   {name} done!')
            
        except Exception as e:
            print(f'   {name} failed: {e}')
            results[name] = {'error': str(e)}
    
    # Save combined results
    with open(os.path.join(output_dir, 'all_neighborhoods.json'), 'w') as f:
        json.dump(results, f, indent=2)
    
    success = sum(1 for r in results.values() if 'error' not in r)
    print(f'\n Done! {success}/{len(polygons)} neighborhoods fetched successfully.')
    print(f'   Results saved to {output_dir}/')
    return results

if __name__ == '__main__':
    fetch_all_neighborhoods()
