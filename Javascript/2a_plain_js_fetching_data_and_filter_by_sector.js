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
const SECTOR = "Emergency Shelter and NFI"
const BASE_URL = `https://stage.hapi-humdata-org.ahconu.org/api/themes/${THEME}?output_format=json&location_code=${LOCATION}&sector_name=${SECTOR}`;
const LIMIT = 1000;

window.onload = async function() {
    const results = await fetchData(BASE_URL, LIMIT);
    console.log(results);
};