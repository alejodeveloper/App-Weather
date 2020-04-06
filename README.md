# App-Weather
API to connect know weather

### App-Weather install

After clone the repo
```
cd where_repo_was_clone
make start-dev
```

This should be run the project in `localhost` over the PORT `8000`

### Basic Requests V1
##### GET URL `api/v1/weather` 
Parameters `city: String` `country: String` 

test_example_url `localhost:8000/api/v1/weather?city=London&country=uk`

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