# HAPI-Code-Examples

## 1. Query a theme end point and loop through pages

### Python

```python
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

const BASE_URL = "https://stage.hapi-humdata-org.ahconu.org/api/themes/3w?output_format=json";
const LIMIT = 1000;

fetchData(BASE_URL, LIMIT).then(results => {
    console.log(results);
});
```

### Javascript

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

const BASE_URL = "https://stage.hapi-humdata-org.ahconu.org/api/themes/3w?output_format=json";
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

const BASE_URL = "https://stage.hapi-humdata-org.ahconu.org/api/themes/3w?output_format=json";
const LIMIT = 1000;

fetchData(BASE_URL, LIMIT).then(results => {
    console.log(results);
});
```

## 2. Query 3W end point and loop through pages

### Python

### Javascript

## 3. Query Population end point and filter for Female Population

### Python

### Javascript

## 4. Query 3W end point and filter for health sector

### Python

### Javascript

## 5. Get admin level data for a country

## 6. Query Population and join to GeoJson from ITOS service

### Python

### Javascript

## 7. Query 3W from 3 countries and join data together

### Python

### Javascript

## 8. Load data intoa google spreadsheet using app script and periodically update

### App script

## 9. Get admin level data for a country