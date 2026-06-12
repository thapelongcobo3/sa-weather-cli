import requests


def getCoordinates(city):
    cityUrl = f"https://nominatim.openstreetmap.org/search?q={city.title()}&format=json&limit=1"
    headers = {"User-Agent": "weather-cli/1.0"}
    cityUrlResponse = requests.get(cityUrl, headers=headers).json()
    if not cityUrlResponse:
        print(f"City '{city}' not found. Please try again.")
        exit()
    latitude = cityUrlResponse[0]["lat"]
    longitude = cityUrlResponse[0]["lon"]
    return latitude, longitude


def getWeather(latitude, longitude):
    weatherURL = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m&timezone=Africa/Johannesburg"
    weatherURLResponse = requests.get(weatherURL).json()
    temperature = f"{weatherURLResponse["current"]["temperature_2m"]}{weatherURLResponse["current_units"]["temperature_2m"]}"
    humidity = f"{weatherURLResponse["current"]["relative_humidity_2m"]}{weatherURLResponse["current_units"]["relative_humidity_2m"]}"
    return temperature, humidity


city = input("Enter city: ")
latitude, longitude = getCoordinates(city)
temperature, humidity = getWeather(latitude, longitude)


print(f"{city.title()}, South Africa\nTemperature: {temperature}\nHumidity: {humidity}")
