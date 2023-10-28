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
        
        with urllib.request.urlopen(url) as response:
            print(f"Getting results {offset} to {offset+limit-1}")
            json_response = json.loads(response.read())
            
            results.extend(json_response)
            
            # If the returned results are less than the limit, it's the last page
            if len(json_response) < limit:
                break
        
        idx += 1
        
    return results

THEME = "3w"
LOCATION = "AFG"
SECTOR= urllib.parse.quote("Emergency Shelter and NFI")
BASE_URL = f"https://stage.hapi-humdata-org.ahconu.org/api/themes/{THEME}?output_format=json&location_code={LOCATION}&sector_name={SECTOR}"
LIMIT = 1000


results = fetch_data(BASE_URL, LIMIT)
print(results)