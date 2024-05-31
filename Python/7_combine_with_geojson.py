import urllib.request
import json

def fetch_data(base_url, limit=1000):
    """
    Fetch data from the provided base_url with pagination support.
    
    Args:
    - base_url (str): The base URL endpoint to fetch data from.
    - limit (int): The number of records to fetch per request.
    
    Returns:
    - list: A list of fetched results.
    """
    
    idx = 0
    results = []
    
    while True:
        offset = idx * limit
        url = f"{base_url}&offset={offset}&limit={limit}"
        print(url)
        with urllib.request.urlopen(url) as response:
            print(f"Getting results {offset} to {offset+limit-1}")
            json_response = json.loads(response.read())
            
            results.extend(json_response['data'])
            
            # If the returned results are less than the limit, it's the last page
            if len(json_response['data']) < limit:
                break
        
        idx += 1
        
    return results

def download_geojson(geojson_url):
    """
    Download GeoJSON data from the provided URL.
    
    Args:
    - geojson_url (str): The URL to download the GeoJSON data from.
    
    Returns:
    - dict: The GeoJSON data as a dictionary.
    """
    with urllib.request.urlopen(geojson_url) as response:
        print("Downloading GeoJSON data...")
        return json.loads(response.read())

def append_population_to_geojson(geojson, population_data):
    """
    Append population data to the GeoJSON properties.
    
    Args:
    - geojson (dict): The GeoJSON data.
    - population_data (list): The population data to append.
    
    Returns:
    - dict: The updated GeoJSON data.
    """
    for feature in geojson['features']:
        feature_id = feature['properties']['ADM1_PCODE']
        corresponding_data = next((item for item in population_data if item['admin1_code'] == feature_id), None)
        if corresponding_data:
             feature['properties']['population_f_80+'] = corresponding_data['population']
        pass

    return geojson

def save_geojson(geojson, filename):
    """
    Save the GeoJSON data to a file.
    
    Args:
    - geojson (dict): The GeoJSON data.
    - filename (str): The filename to save the data to.
    """
    with open(filename, 'w') as file:
        json.dump(geojson, file)
        print(f"GeoJSON saved to {filename}")

THEME = "population-social/population"
LOCATION = "AFG"
AGE_RANGE_CODE = "0-4"
GENDER = "f"
BASE_URL = f"https://stage.hapi-humdata-org.ahconu.org/api/v1/{THEME}?output_format=json&location_code={LOCATION}&age_range_code={AGE_RANGE_CODE}&gender={GENDER}&admin_level=1&app_identifier={ your app identifier }"
LIMIT = 1000
results = fetch_data(BASE_URL, LIMIT)

geojson_url = "https://apps.itos.uga.edu/codv2api/api/v1/themes/cod-ab/locations/AFG/versions/current/geoJSON/1"
geojson_data = download_geojson(geojson_url)
updated_geojson = append_population_to_geojson(geojson_data, results)
save_geojson(updated_geojson, 'updated_data.geojson')