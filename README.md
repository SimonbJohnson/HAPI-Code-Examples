# HAPI-Code-Examples

## 1. Query a theme end point and loop through pages

Themes are the core data of the API.  The results are paginated and so multiple calls are needed to get the whole dataset.  Below we query the 3W theme for Afghanistan and return all results into a single object.  To query a different theme or country change the constant variable of ```THEME``` to another theme or ```LOCATION``` to a different ISO3 country code.

The current themes supported ```population```, ```3w```.

The current countries supported ```AFG```, ```MLI```, ```NGA```

### Python

```python
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
BASE_URL = f"https://stage.hapi-humdata-org.ahconu.org/api/themes/{THEME}?output_format=json&location_code={LOCATION}"
LIMIT = 1000


results = fetch_data(BASE_URL, LIMIT)
print(results)
```

### Plain Javascript

```javascript
async function fetchData(baseUrl, limit = 1000) {
    let idx = 0;
    let results = [];

    while (true) {
        const offset = idx * limit;
        const url = `${baseUrl}&offset=${offset}&limit=${limit}`;

        console.log(`Getting results ${offset} to ${offset + limit - 1}`);
        
        const response = await fetch(url);
        const jsonResponse = await response.json();

        results = results.concat(jsonResponse);

        // If the returned results are less than the limit, it's the last page
        if (jsonResponse.length < limit) {
            break;
        }

        idx++;
    }

    return results;
}

const THEME = "3W"
const LOCATION = "AFG"
const BASE_URL = `https://stage.hapi-humdata-org.ahconu.org/api/themes/${THEME}?output_format=json&location_code=${LOCATION}`;
const LIMIT = 1000;

window.onload = async function() {
    const results = await fetchData(BASE_URL, LIMIT);
    console.log(results);
};
```

### Node

```javascript
import fetch from 'node-fetch'

async function fetchData(baseUrl, limit = 1000) {
    let idx = 0;
    let results = [];

    while (true) {
        const offset = idx * limit;
        const url = `${baseUrl}&offset=${offset}&limit=${limit}`;

        console.log(`Getting results ${offset} to ${offset + limit - 1}`);
        
        const response = await fetch(url);
        const jsonResponse = await response.json();

        results = results.concat(jsonResponse);

        // If the returned results are less than the limit, it's the last page
        if (jsonResponse.length < limit) {
            break;
        }

        idx++;
    }

    return results;
}

const THEME = "3W"
const LOCATION = "AFG"
const BASE_URL = `https://stage.hapi-humdata-org.ahconu.org/api/themes/${THEME}?output_format=json&location_code=${LOCATION}`;
const LIMIT = 1000;

fetchData(BASE_URL, LIMIT).then(results => {
    console.log(results);
});
```

### R

```R
library(jsonlite)
library(httr)

fetch_data <- function(base_url, limit = 1000) {
  idx <- 0
  results <- list()
  
  while(TRUE) {
    offset <- idx * limit
    url <- paste0(base_url, "&offset=", offset, "&limit=", limit)
    
    response <- GET(url)
    
    cat("Getting results", offset, "to", offset + limit - 1, "\n")
    
    json_response <- fromJSON(content(response, "text"))
    
    results <- append(results, list(json_response))
    
    # If the returned results are less than the limit, it's the last page
    if(length(json_response) < limit) {
      break
    }
    
    idx <- idx + 1
  }
  
  return(results)
}

THEME <- "3w"
LOCATION <- "AFG"
BASE_URL <- paste0("https://stage.hapi-humdata-org.ahconu.org/api/themes/", THEME, "?output_format=json&location_code=", LOCATION)
LIMIT <- 1000

results <- fetch_data(BASE_URL, LIMIT)
print(results)
```

## 2. Filtering results

It is possible to add extra filters to the call to get a subset of results. To see the full set of filters that can be used for each theme, please check this documentation:

https://stage.hapi-humdata-org.ahconu.org/docs#/humanitarian-response/

### Python

#### Filter by Sector

Change the code to include a new parameter in the URL. Please check the example repository for the full code.

```python
SECTOR= urllib.parse.quote("Emergency Shelter and NFI")
BASE_URL = f"https://stage.hapi-humdata-org.ahconu.org/api/themes/{THEME}?output_format=json&location_code={LOCATION}&sector_name={SECTOR}"
```

#### Filter by Admin1

```python
ADMIN1= "AF01"
BASE_URL = f"https://stage.hapi-humdata-org.ahconu.org/api/themes/{THEME}?output_format=json&location_code={LOCATION}&admin1_code={ADMIN1}"
```

### Plain Javascript and Node

Change the code to include a new parameter in the URL. Please check the example repository for the full code.

#### Filter by Sector

```javascript
const SECTOR = "Emergency Shelter and NFI"
const BASE_URL = `https://stage.hapi-humdata-org.ahconu.org/api/themes/${THEME}?output_format=json&location_code=${LOCATION}&sector_name=${SECTOR}`;
```

#### Filter by Admin1

```javascript
const ADMIN1 = "AF01"
const BASE_URL = `https://stage.hapi-humdata-org.ahconu.org/api/themes/${THEME}?output_format=json&location_code=${LOCATION}&admin1_code=${ADMIN1}`;
```

## 3. Get data from supporting tables

Each supporting table such as ```orgs```, ```orgs_type```, ```sector``` and more have a unique URL to call to get the range of possible values.  Below we show the URL for getting of the sector names and codes.  Change the code at the top to have a new ```BASEURL``` and remove the URL parameters above it. Full code examples can be seen in the example repo.

### Python

```python
BASE_URL "https://stage.hapi-humdata-org.ahconu.org/api/sector?output_format=json&offset=0&limit=1000"
```

### Javascript

```javascript
CONST BASE_URL "https://stage.hapi-humdata-org.ahconu.org/api/sector?output_format=json&offset=0&limit=1000"
```

## 4. Get admin level data for a country

The admin1 and admin2 api end points provide data about subnational adminstration boundary names and p-codes (place codes). The geometry associated with each admin boundary is not yet available via the API, but it can be downloaded from HDX or obtained from the ITOS API service.  To query the adminstration area endputs use the URL below

```python
BASE_URL = "https://stage.hapi-humdata-org.ahconu.org/api/admin1?location_code=MLI&output_format=json&offset=0&limit=1000"
```

### Javascript

```javascript
CONST BASE_URL = "https://stage.hapi-humdata-org.ahconu.org/api/admin1?location_code=MLI&output_format=json&offset=0&limit=1000"
```

### Python

### Javascript

## 5. Download as CSV

The code examples so far have been using JSON output and then processing this data. To query this data as csv, change the output format to csv as per the examples below. Visiting this URL through the browser will download the CSV to then be used on your computer.

```python
BASE_URL = "https://stage.hapi-humdata-org.ahconu.org/api/admin1?location_code=MLI&output_format=csv&offset=0&limit=1000"
```

### Javascript

```javascript
CONST BASE_URL = "https://stage.hapi-humdata-org.ahconu.org/api/admin1?location_code=MLI&output_format=csv&offset=0&limit=1000"
```

## 6. Query Population and join to GeoJson from ITOS service

### Python

### Javascript

## 7. Load data intoa google spreadsheet using app script and periodically update

### App script

#### 1. Create a New Google Spreadsheet:

Create a new Google Spreadsheet where you want to load the data.

#### 2. Open the Script Editor:

Click on Extensions -> Apps Script in the top menu to open the Google Apps Script editor.

#### 3. Use this code

A simple script that will fetch the API data and place it in the spreadsheet

```javascript
function loadApiData() {
  var baseUrl = "https://stage.hapi-humdata-org.ahconu.org/api/themes/3w?output_format=json";
  var limit = 10000;
  var offset = 0;
  
  var allData = [];

  while (true) {
    // Fetch data from the current page
    var url = baseUrl + "&offset=" + offset + "&limit=" + limit;
    var response = UrlFetchApp.fetch(url);
    var jsonData = JSON.parse(response.getContentText());
    
    // If there's no data or less data than the limit, break out of the loop
    if (!jsonData.length || jsonData.length < limit) {
      allData = allData.concat(jsonData);
      break;
    }

    // Otherwise, store the data and increment the offset for the next page
    allData = allData.concat(jsonData);
    offset += limit;
  }

  // Convert the JSON data to a 2D array for the spreadsheet
  var dataArray = [];
  
  // If there's data, add headers from the first item's keys
  if (allData.length > 0) {
    dataArray.push(Object.keys(allData[0]));
  }

  allData.forEach(function(item) {
    var row = [];
    for (var key in item) {
      row.push(item[key]);
    }
    dataArray.push(row);
  });

  // Get the active sheet and clear existing data
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  sheet.clear();

  // Write the headers and data to the spreadsheet
  if (dataArray.length > 0) {
    sheet.getRange(1, 1, dataArray.length, dataArray[0].length).setValues(dataArray);
  }
}

```

#### 4. Set up a Daily Trigger:

- Click on the clock icon on the left sidebar to view the project's triggers.
- Click on the + Add Trigger button at the bottom right.
- Set the function to loadApiData, the deployment to Head, the event source to Time-driven, and then select Day timer to choose a specific time of day.
- Click Save.

#### 5. Authorize the Script:

When you run the script for the first time or set up a trigger, it will ask for permissions. Make sure to grant them so the script can access the external API and modify your Google Spreadsheet.

Now, the script will run daily at the time you specified and load the API data into your Google Spreadsheet.