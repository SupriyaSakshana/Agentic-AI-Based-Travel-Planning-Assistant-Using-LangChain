import requests

def get_weather(query):

    # -----------------------------------
    # HANDLE DICTIONARY INPUT
    # -----------------------------------

    if isinstance(query, dict):

        city = query.get("city", "")

    # -----------------------------------
    # HANDLE STRING INPUT
    # -----------------------------------

    elif isinstance(query, str):

        city = query

    else:
        return "Invalid weather input."


    # -----------------------------------
    # CITY → LATITUDE/LONGITUDE MAPPING
    # -----------------------------------

    city_coordinates = {

        "goa": {
            "latitude": 15.2993,
            "longitude": 74.1240
        },

        "delhi": {
            "latitude": 28.6139,
            "longitude": 77.2090
        },

        "manali": {
            "latitude": 32.2432,
            "longitude": 77.1892
        },

        "mumbai": {
            "latitude": 19.0760,
            "longitude": 72.8777
        },

        "jaipur": {
            "latitude": 26.9124,
            "longitude": 75.7873
        }
    }


    city_lower = city.lower()


    # -----------------------------------
    # VALIDATION
    # -----------------------------------

    if city_lower not in city_coordinates:

        return "Weather data not available for this city."


    latitude = city_coordinates[city_lower]["latitude"]
    longitude = city_coordinates[city_lower]["longitude"]


    # -----------------------------------
    # WEATHER API
    # -----------------------------------

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}"
        f"&longitude={longitude}"
        f"&current_weather=true"
    )


    # -----------------------------------
    # API REQUEST
    # -----------------------------------

    try:

        response = requests.get(url)

        data = response.json()

        current = data.get("current_weather", {})

        temperature = current.get("temperature", "N/A")
        windspeed = current.get("windspeed", "N/A")

        return f"""
        🌤 Weather Forecast

        City: {city.title()}

        Temperature: {temperature}°C
        Wind Speed: {windspeed} km/h
        """

    except Exception as e:

        return f"Weather API Error: {str(e)}"