"""
Configuration and Indian Administrative Geography Data
Supports States, Union Territories, and Major Districts (e.g., Mumbai divided into 100 sectors).
"""
import os

PORT = int(os.environ.get("PORT", 8000))
GOOGLE_MAPS_API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY", "")

# Curated Bounding Boxes for Indian States & Districts
# Format: [south_lat, west_lng, north_lat, east_lng], default_center: [lat, lng], default_zoom: int
INDIAN_REGIONS = {
    # Districts / Metropolitan Zones
    "mumbai": {
        "name": "Mumbai (100 Sectors)",
        "type": "district",
        "state": "Maharashtra",
        "bounds": [18.8900, 72.7750, 19.2800, 72.9850],
        "center": [19.0760, 72.8777],
        "zoom": 12,
        "default_grid": [10, 10], # 100 sectors
        "tilt": 62,
        "heading": 15
    },
    "delhi_ncr": {
        "name": "Delhi NCR (100 Sectors)",
        "type": "district",
        "state": "Delhi",
        "bounds": [28.4000, 76.8500, 28.8800, 77.4000],
        "center": [28.6139, 77.2090],
        "zoom": 12,
        "default_grid": [10, 10],
        "tilt": 60,
        "heading": 0
    },
    "bengaluru": {
        "name": "Bengaluru Urban (100 Sectors)",
        "type": "district",
        "state": "Karnataka",
        "bounds": [12.8300, 77.4500, 13.1500, 77.7800],
        "center": [12.9716, 77.5946],
        "zoom": 12,
        "default_grid": [10, 10],
        "tilt": 60,
        "heading": 20
    },
    "pune": {
        "name": "Pune City (64 Sectors)",
        "type": "district",
        "state": "Maharashtra",
        "bounds": [18.4200, 73.7400, 18.6300, 73.9800],
        "center": [18.5204, 73.8567],
        "zoom": 12,
        "default_grid": [8, 8],
        "tilt": 55,
        "heading": 10
    },
    "hyderabad": {
        "name": "Hyderabad (64 Sectors)",
        "type": "district",
        "state": "Telangana",
        "bounds": [17.2800, 78.3000, 17.5500, 78.6000],
        "center": [17.3850, 78.4867],
        "zoom": 12,
        "default_grid": [8, 8],
        "tilt": 55,
        "heading": 0
    },
    "chennai": {
        "name": "Chennai (64 Sectors)",
        "type": "district",
        "state": "Tamil Nadu",
        "bounds": [12.9200, 80.1200, 13.2000, 80.3200],
        "center": [13.0827, 80.2707],
        "zoom": 12,
        "default_grid": [8, 8],
        "tilt": 55,
        "heading": 350
    },
    "kolkata": {
        "name": "Kolkata (64 Sectors)",
        "type": "district",
        "state": "West Bengal",
        "bounds": [22.4500, 88.2500, 22.6800, 88.4500],
        "center": [22.5726, 88.3639],
        "zoom": 12,
        "default_grid": [8, 8],
        "tilt": 55,
        "heading": 5
    },
    "ahmedabad": {
        "name": "Ahmedabad (64 Sectors)",
        "type": "district",
        "state": "Gujarat",
        "bounds": [22.9200, 72.4500, 23.1500, 72.6800],
        "center": [23.0225, 72.5714],
        "zoom": 12,
        "default_grid": [8, 8],
        "tilt": 55,
        "heading": 0
    },

    # Indian States
    "maharashtra": {
        "name": "Maharashtra State",
        "type": "state",
        "bounds": [15.6000, 72.6000, 22.0000, 80.9000],
        "center": [19.7515, 75.7139],
        "zoom": 7,
        "default_grid": [8, 8],
        "tilt": 45,
        "heading": 0
    },
    "karnataka": {
        "name": "Karnataka State",
        "type": "state",
        "bounds": [11.5000, 74.0000, 18.5000, 78.6000],
        "center": [15.3173, 75.7139],
        "zoom": 7,
        "default_grid": [8, 8],
        "tilt": 45,
        "heading": 0
    },
    "gujarat": {
        "name": "Gujarat State",
        "type": "state",
        "bounds": [20.1000, 68.1000, 24.7000, 74.5000],
        "center": [22.2587, 71.1924],
        "zoom": 7,
        "default_grid": [8, 8],
        "tilt": 45,
        "heading": 0
    },
    "tamil_nadu": {
        "name": "Tamil Nadu State",
        "type": "state",
        "bounds": [8.0500, 76.2000, 13.5500, 80.3500],
        "center": [11.1271, 78.6569],
        "zoom": 7,
        "default_grid": [8, 8],
        "tilt": 45,
        "heading": 0
    },
    "telangana": {
        "name": "Telangana State",
        "type": "state",
        "bounds": [15.8000, 77.2000, 19.9000, 81.8000],
        "center": [18.1124, 79.0193],
        "zoom": 7,
        "default_grid": [8, 8],
        "tilt": 45,
        "heading": 0
    },
    "uttar_pradesh": {
        "name": "Uttar Pradesh State",
        "type": "state",
        "bounds": [23.8500, 77.0500, 30.4000, 84.6500],
        "center": [26.8467, 80.9462],
        "zoom": 7,
        "default_grid": [8, 8],
        "tilt": 45,
        "heading": 0
    },
    "west_bengal": {
        "name": "West Bengal State",
        "type": "state",
        "bounds": [21.5000, 85.8000, 27.2500, 89.9000],
        "center": [22.9868, 87.8550],
        "zoom": 7,
        "default_grid": [8, 8],
        "tilt": 45,
        "heading": 0
    },
    "rajasthan": {
        "name": "Rajasthan State",
        "type": "state",
        "bounds": [23.0500, 69.5000, 30.2000, 78.2500],
        "center": [27.0238, 74.2179],
        "zoom": 6,
        "default_grid": [8, 8],
        "tilt": 45,
        "heading": 0
    },
    "kerala": {
        "name": "Kerala State",
        "type": "state",
        "bounds": [8.3000, 74.8500, 12.8000, 77.4000],
        "center": [10.8505, 76.2711],
        "zoom": 7,
        "default_grid": [8, 8],
        "tilt": 45,
        "heading": 0
    },
    "goa": {
        "name": "Goa",
        "type": "state",
        "bounds": [14.9000, 73.6500, 15.8000, 74.3500],
        "center": [15.2993, 74.1240],
        "zoom": 10,
        "default_grid": [6, 6],
        "tilt": 50,
        "heading": 0
    }
}
