# App-Weather
API to connect Open Weather API and get climate data for a specific city

![alt text](https://upload.wikimedia.org/wikipedia/commons/e/ea/Cirrus-fibratus.jpg)


### App-Weather install

After clone the repo
```
cd where_repo_was_clone
source start.sh;
```

This should be run the project in `localhost` over the PORT `8000`

### Basic Requests V2
##### GET URL `api/v2/weather` 
Parameters `city: String` `country: String` 

test_example_url `localhost:8000/api/v2/weather?city=London&country=uk`

RESPONSE  *200*
```
{
    "location_name": "London, UK",
    "temperature": "12.45 °C",
    "wind": "clear sky, 3.1 m/s, south",
    "cloudiness": "Clear",
    "pressure": "1010 hpa",
    "humidity": "66%",
    "sunrise": "05:23",
    "sunset": "18:41",
    "geo_coordinates": "[51.51 - -0.13]",
    "requested_time": "2020-04-06 02:23"
}
```
RESPONSE  *400*
```
{
    "message_error": "The request must be made with country slug and city slug, current are city None and country None"
}
```

##Version 2 improvements
Add postgres log layer and verify with the logs if a request was made
 within a configurable setting time value and pull it off from database or
 make the request 