from config import NEIGHBORHOODS

def bbox_to_polygon(sw, ne):
    """Convert (sw_lat, sw_lng), (ne_lat, ne_lng) to closed polygon coordinates.
    FortyGuard expects [lng, lat] order (GeoJSON standard).
    """
    sw_lat, sw_lng = sw
    ne_lat, ne_lng = ne
    return [
        [sw_lng, sw_lat],
        [ne_lng, sw_lat],
        [ne_lng, ne_lat],
        [sw_lng, ne_lat],
        [sw_lng, sw_lat]  # close the polygon
    ]

def get_neighborhood_polygons():
    """Get all neighborhood polygons ready for FortyGuard API."""
    polygons = {}
    for name, bbox in NEIGHBORHOODS.items():
        polygons[name] = {
            'coords': bbox_to_polygon(bbox['sw'], bbox['ne']),
            'center_lat': (bbox['sw'][0] + bbox['ne'][0]) / 2,
            'center_lng': (bbox['sw'][1] + bbox['ne'][1]) / 2,
        }
    return polygons

def get_neighborhood_centers():
    """Get center lat/lng for each neighborhood."""
    centers = {}
    for name, bbox in NEIGHBORHOODS.items():
        centers[name] = {
            'lat': (bbox['sw'][0] + bbox['ne'][0]) / 2,
            'lng': (bbox['sw'][1] + bbox['ne'][1]) / 2,
        }
    return centers

if __name__ == '__main__':
    polygons = get_neighborhood_polygons()
    for name, data in polygons.items():
        print(f'{name}: center=({data["center_lat"]:.4f}, {data["center_lng"]:.4f})')
