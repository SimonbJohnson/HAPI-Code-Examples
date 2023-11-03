library(httr)
library(jsonlite)

fetch_data <- function(base_url, limit=1000) {
  results <- list()
  idx <- 0
  
  repeat {
    offset <- idx * limit
    url <- sprintf("%s&offset=%d&limit=%d", base_url, offset, limit)
    print(sprintf("Getting results %d to %d", offset, offset+limit-1))
    
    response <- GET(url)
    stop_for_status(response)
    json_response <- content(response, "parsed", type = "application/json")
    
    results <- c(results, json_response)
    
    if (length(json_response) < limit) {
      break
    }
    idx <- idx + 1
  }
  
  return(results)
}

download_geojson <- function(geojson_url) {
  print("Downloading GeoJSON data...")
  response <- GET(geojson_url)
  stop_for_status(response)
  geojson_data <- content(response, "parsed", type = "application/json")
  return(geojson_data)
}

append_population_to_geojson <- function(geojson, population_data) {
  geojson$features <- lapply(geojson$features, function(feature) {
    feature_id <- feature$properties$ADM1_PCODE
    corresponding_data <- Filter(function(item) item$admin1_code == feature_id, population_data)
    if (length(corresponding_data) > 0) {
      feature$properties$population_f_80plus <- corresponding_data[[1]]$population
    }
    return(feature)
  })
  return(geojson)
}

save_geojson <- function(geojson, filename) {
  write_json(geojson, filename)
  print(paste("GeoJSON saved to", filename))
}

# Use the functions
THEME <- "population"
LOCATION <- "AFG"
AGE_RANGE_CODE <- "80%2B"
GENDER <- "f"
BASE_URL <- sprintf("https://stage.hapi-humdata-org.ahconu.org/api/themes/%s?output_format=json&location_code=%s&age_range_code=%s&gender=%s&admin1_is_unspecified=false&admin2_is_unspecified=true",
                    THEME, LOCATION, AGE_RANGE_CODE, GENDER)
LIMIT <- 1000
results <- fetch_data(BASE_URL, LIMIT)

geojson_url <- "https://apps.itos.uga.edu/codv2api/api/v1/themes/cod-ab/locations/AFG/versions/current/geoJSON/1"
geojson_data <- download_geojson(geojson_url)
updated_geojson <- append_population_to_geojson(geojson_data, results)
save_geojson(updated_geojson, 'updated_data.geojson')