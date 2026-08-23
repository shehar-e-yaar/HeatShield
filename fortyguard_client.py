import requests
import time
import json
from config import API_KEY, BASE_URL, POLL_INTERVAL_SECONDS, MAX_POLL_RETRIES

class FortyGuardClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or API_KEY
        self.headers = {
            'api-key': self.api_key,
            'Content-Type': 'application/json'
        }
    
    def submit_heatmap(self, polygon_coords, start_date, filter_type=3, granularity=100, start_time=None, end_time=None, end_date=None):
        """Submit a heatmap generation request.
        
        Args:
            polygon_coords: list of [lng, lat] pairs forming a closed polygon
            start_date: 'YYYY-MM-DD' format
            filter_type: 1=single hour, 2=hour range, 3=single day, 4=day range
            granularity: 60, 80, or 100
        """
        payload = {
            'polygon_aoi': {
                'type': 'FeatureCollection',
                'features': [{
                    'type': 'Feature',
                    'properties': {},
                    'geometry': {
                        'type': 'Polygon',
                        'coordinates': [polygon_coords]
                    }
                }]
            },
            'date_time': {
                'start_date': start_date,
                'filter_type': filter_type
            },
            'granularity': granularity
        }
        if start_time:
            payload['date_time']['start_time'] = start_time
        if end_time:
            payload['date_time']['end_time'] = end_time
        if end_date:
            payload['date_time']['end_date'] = end_date
        
        response = requests.post(f'{BASE_URL}/heatmap', headers=self.headers, json=payload)
        response.raise_for_status()
        data = response.json()
        if data.get('error'):
            raise Exception(f"API error: {data.get('message')}")
        return data['data']['activity_id']
    
    def submit_env_params(self, latitude, longitude, temperature, start_date, filter_type=1, start_time=None, analysis=None):
        """Submit environmental parameters request."""
        payload = {
            'latitude': latitude,
            'longitude': longitude,
            'temperature': temperature,
            'date_time': {
                'start_date': start_date,
                'filter_type': filter_type
            }
        }
        if start_time:
            payload['date_time']['start_time'] = start_time
        if analysis:
            payload['analysis'] = analysis
        
        response = requests.post(f'{BASE_URL}/env_params', headers=self.headers, json=payload)
        response.raise_for_status()
        data = response.json()
        if data.get('error'):
            raise Exception(f"API error: {data.get('message')}")
        return data['data']['activity_id']
    
    def submit_satellite(self, latitude, longitude, start_date, filter_type=1, start_time='14:00', granularity=80):
        payload = {
            'sat': {'latitude': latitude, 'longitude': longitude},
            'date_time': {'start_date': start_date, 'start_time': start_time, 'filter_type': filter_type},
            'granularity': granularity
        }
        response = requests.post(f'{BASE_URL}/satellite', headers=self.headers, json=payload)
        response.raise_for_status()
        data = response.json()
        if data.get('error'):
            raise Exception(f"API error: {data.get('message')}")
        return data['data']['activity_id']
    
    def poll_status(self, activity_id, verbose=True):
        """Poll task status until completed or failed."""
        url = f'{BASE_URL}/status/{activity_id}'
        for attempt in range(MAX_POLL_RETRIES):
            try:
                response = requests.get(url, headers={'api-key': self.api_key}, timeout=30)
                response.raise_for_status()
                data = response.json()['data']
                status = data.get('status', '').lower()
                
                if status in ('completed', 'succeeded'):
                    if verbose:
                        print(f'   Task {activity_id[:8]}... completed!')
                    return data
                elif status in ('failed', 'error'):
                    raise RuntimeError(f'Task {activity_id} failed: {data}')
                else:
                    if verbose and attempt % 6 == 0:
                        print(f'  ⏳ Task {activity_id[:8]}... processing (attempt {attempt+1})')
                    time.sleep(POLL_INTERVAL_SECONDS)
            except requests.exceptions.RequestException as e:
                if verbose:
                    print(f'   Network error on attempt {attempt+1}: {e}')
                time.sleep(POLL_INTERVAL_SECONDS)
        
        raise TimeoutError(f'Task {activity_id} did not complete after {MAX_POLL_RETRIES} attempts')
    
    def submit_and_wait(self, submit_fn, *args, **kwargs):
        """Submit a task and wait for result."""
        activity_id = submit_fn(*args, **kwargs)
        return self.poll_status(activity_id)
