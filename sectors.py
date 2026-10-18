"""
Sector Grid Generator & Spatial Indexing for Indian Regions
Subdivides States, Districts, and Cities (like Mumbai into 100 sectors).
"""
import math
from typing import List, Dict, Any, Optional
from config import INDIAN_REGIONS

# Known landmarks for semantic naming of sectors in Mumbai
MUMBAI_LANDMARKS = [
    {"name": "Colaba & Gateway", "lat": 18.9067, "lng": 72.8147},
    {"name": "Nariman Point & Marine Drive", "lat": 18.9256, "lng": 72.8242},
    {"name": "Fort & CST Heritage Zone", "lat": 18.9400, "lng": 72.8350},
    {"name": "Churchgate & Oval", "lat": 18.9322, "lng": 72.8264},
    {"name": "Byculla & Mazgaon Docks", "lat": 18.9750, "lng": 72.8380},
    {"name": "Malabar Hill & Breach Candy", "lat": 18.9550, "lng": 72.8050},
    {"name": "Worli Sea Face & Lower Parel", "lat": 19.0020, "lng": 72.8250},
    {"name": "Dadar West & Shivaji Park", "lat": 19.0260, "lng": 72.8370},
    {"name": "Dadar East & Wadala", "lat": 19.0200, "lng": 72.8550},
    {"name": "Mahim Bay & Dharavi Tech Hub", "lat": 19.0400, "lng": 72.8450},
    {"name": "Bandra West & Carter Road", "lat": 19.0600, "lng": 72.8300},
    {"name": "BKC (Bandra Kurla Complex)", "lat": 19.0670, "lng": 72.8680},
    {"name": "Khar West & Linking Road", "lat": 19.0700, "lng": 72.8330},
    {"name": "Santacruz & Kalina Campus", "lat": 19.0800, "lng": 72.8550},
    {"name": "Juhu Beach & Vile Parle West", "lat": 19.1000, "lng": 72.8280},
    {"name": "Domestic Airport & Vile Parle East", "lat": 19.0980, "lng": 72.8530},
    {"name": "Andheri West & Lokhandwala", "lat": 19.1360, "lng": 72.8270},
    {"name": "Andheri East & MIDC SEEPZ", "lat": 19.1200, "lng": 72.8680},
    {"name": "Jogeshwari & Western Express", "lat": 19.1400, "lng": 72.8500},
    {"name": "Goregaon West & Inorbit Area", "lat": 19.1650, "lng": 72.8450},
    {"name": "Goregaon East & Film City", "lat": 19.1680, "lng": 72.8850},
    {"name": "Malad West & Mindspace BPO", "lat": 19.1850, "lng": 72.8380},
    {"name": "Kandivali West & Mahavir Nagar", "lat": 19.2080, "lng": 72.8420},
    {"name": "Kandivali East & Thakur Complex", "lat": 19.2100, "lng": 72.8700},
    {"name": "Borivali West & IC Colony", "lat": 19.2300, "lng": 72.8500},
    {"name": "Borivali East & National Park Border", "lat": 19.2290, "lng": 72.8650},
    {"name": "Dahisar West & Toll Naka", "lat": 19.2550, "lng": 72.8600},
    {"name": "Kurla West & Phoenix Marketcity", "lat": 19.0700, "lng": 72.8800},
    {"name": "Ghatkopar East & R-City", "lat": 19.0850, "lng": 72.9080},
    {"name": "Chembur Commercial Belt", "lat": 19.0550, "lng": 72.8980},
    {"name": "Vikhroli & Godrej One Zone", "lat": 19.1100, "lng": 72.9250},
    {"name": "Powai & Hiranandani Tech Park", "lat": 19.1250, "lng": 72.9100},
    {"name": "Bhandup Industrial Complex", "lat": 19.1500, "lng": 72.9400},
    {"name": "Mulund West & LBS Marg", "lat": 19.1750, "lng": 72.9550},
    {"name": "Thane Border Corridor", "lat": 19.1950, "lng": 72.9750},
]

def calculate_distance(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    """Haversine formula approximation in km."""
    R = 6371.0
    dlat = math.radians(lat2 - lat1)
    dlng = math.radians(lng2 - lng1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlng / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def find_nearest_landmark(lat: float, lng: float, region_key: str) -> str:
    """Finds closest landmark name to contextualize the sector."""
    if region_key == "mumbai":
        best_name = None
        min_dist = float("inf")
        for lm in MUMBAI_LANDMARKS:
            d = calculate_distance(lat, lng, lm["lat"], lm["lng"])
            if d < min_dist:
                min_dist = d
                best_name = lm["name"]
        if min_dist <= 2.8:
            return f"{best_name}"
        else:
            return f"Near {best_name}"
    return "Sector Zone"

def generate_sectors_for_region(region_key: str, rows: Optional[int] = None, cols: Optional[int] = None) -> Dict[str, Any]:
    """
    Subdivides any Indian State or District into a grid of sectors.
    For Mumbai, default is 10 rows x 10 cols = 100 sectors.
    """
    region_info = INDIAN_REGIONS.get(region_key)
    if not region_info:
        # Fallback to Mumbai if unknown
        region_key = "mumbai"
        region_info = INDIAN_REGIONS["mumbai"]

    south, west, north, east = region_info["bounds"]
    
    if rows is None or cols is None:
        rows, cols = region_info.get("default_grid", [10, 10])

    lat_step = (north - south) / rows
    lng_step = (east - west) / cols

    sectors = []
    sector_idx = 1

    # Generate from South to North, West to East
    for r in range(rows):
        for c in range(cols):
            s_lat = south + r * lat_step
            n_lat = south + (r + 1) * lat_step
            w_lng = west + c * lng_step
            e_lng = west + (c + 1) * lng_step

            center_lat = (s_lat + n_lat) / 2
            center_lng = (w_lng + e_lng) / 2

            locality = find_nearest_landmark(center_lat, center_lng, region_key)
            sector_code = f"SEC-{sector_idx:03d}"

            # Calculate approx 3D camera heading (orbiting inward)
            heading = 15.0 + (c % 3) * 10

            sector_data = {
                "id": sector_code,
                "index": sector_idx,
                "row": r,
                "col": c,
                "name": f"{sector_code}: {locality}",
                "locality": locality,
                "region_key": region_key,
                "bounds": {
                    "south": round(s_lat, 6),
                    "west": round(w_lng, 6),
                    "north": round(n_lat, 6),
                    "east": round(e_lng, 6)
                },
                "center": {
                    "lat": round(center_lat, 6),
                    "lng": round(center_lng, 6)
                },
                "polygon": [
                    {"lat": round(s_lat, 6), "lng": round(w_lng, 6)},
                    {"lat": round(n_lat, 6), "lng": round(w_lng, 6)},
                    {"lat": round(n_lat, 6), "lng": round(e_lng, 6)},
                    {"lat": round(s_lat, 6), "lng": round(e_lng, 6)}
                ],
                "camera_3d": {
                    "center": {"lat": round(center_lat, 6), "lng": round(center_lng, 6)},
                    "tilt": 62,
                    "heading": heading,
                    "zoom": 15.5
                },
                "status": "idle", # idle, scraping, ready
                "stats": {
                    "total_businesses": 0,
                    "no_website": 0,
                    "crap_website": 0,
                    "good_website": 0
                }
            }
            sectors.append(sector_data)
            sector_idx += 1

    return {
        "region_key": region_key,
        "region_name": region_info["name"],
        "region_type": region_info["type"],
        "total_sectors": len(sectors),
        "grid": {"rows": rows, "cols": cols},
        "bounds": region_info["bounds"],
        "center": region_info["center"],
        "zoom": region_info["zoom"],
        "tilt": region_info.get("tilt", 55),
        "heading": region_info.get("heading", 0),
        "sectors": sectors
    }
