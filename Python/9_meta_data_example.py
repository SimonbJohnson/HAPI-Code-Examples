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

URL = f"https://stage.hapi-humdata-org.ahconu.org/api/themes/population?gender_code=f&age_range_code=0-4&resource_update_date_min=2020-01-01&resource_update_date_max=2024-12-31&admin2_name=Awka%20North&output_format=json"
LIMIT = 1000

results = fetch_data(BASE_URL, LIMIT)
print(results[0])
resource_id = results[0]["resource_hdx_id"]

URL_META = f"https://stage.hapi-humdata-org.ahconu.org/api/resource?hdx_id={resource_id}&update_date_min=2020-01-01&update_date_max=2024-12-31&output_format=json&offset=0&limit=1000"
