import requests
import json

# Returns tuple (lat, long)
def get_ip_lat_log(ip_address=""):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}?fields=lat,lon")
        response.raise_for_status()
        data = response.json()
        return data["lat"], data["lon"]
    except Exception as e:
        print(f"Error getting IP: {e}")
        return (37.7749, -122.4194)