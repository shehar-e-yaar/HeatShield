import os
from dotenv import load_dotenv

load_dotenv()

# FortyGuard API
API_KEY = os.getenv('FORTYGUARD_API_KEY', '')
BASE_URL = 'https://api.fortyguard.com/v1'

# City: Los Angeles, CA
CITY_NAME = 'Los Angeles, CA'
CITY_CENTER = (34.0522, -118.2437)

# Los Angeles neighborhoods with bounding boxes (SW corner, NE corner)
# These define the polygons we'll send to the heatmap API
NEIGHBORHOODS = {
    'Downtown LA': {'sw': (34.030, -118.270), 'ne': (34.060, -118.230)},
    'Boyle Heights': {'sw': (34.020, -118.220), 'ne': (34.050, -118.180)},
    'Hollywood': {'sw': (34.080, -118.350), 'ne': (34.110, -118.310)},
    'Van Nuys': {'sw': (34.170, -118.470), 'ne': (34.200, -118.430)},
    'Compton': {'sw': (33.880, -118.240), 'ne': (33.910, -118.200)},
    'Santa Monica': {'sw': (34.000, -118.500), 'ne': (34.030, -118.460)},
    'Pacoima': {'sw': (34.250, -118.440), 'ne': (34.280, -118.400)},
    'Echo Park': {'sw': (34.060, -118.270), 'ne': (34.090, -118.240)},
    'South LA': {'sw': (33.960, -118.300), 'ne': (33.990, -118.260)},
    'Encino': {'sw': (34.140, -118.520), 'ne': (34.170, -118.480)}
}

# Default scoring weights
DEFAULT_WEIGHTS = {
    'heat': 40,
    'population': 35,
    'tree_cover': 15,
    'pavement': 10
}

# API limits
MAX_HEATMAP_AREA_MI2 = 10  # Basic plan limit
POLL_INTERVAL_SECONDS = 5
MAX_POLL_RETRIES = 120

# Data directories
RAW_DATA_DIR = 'data/raw'
PROCESSED_DATA_DIR = 'data/processed'
