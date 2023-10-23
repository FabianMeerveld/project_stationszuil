import requests

key = "b843235546375e04da44b6fb8b10f175"


def GetWeather(location):  # location = str (plaatsnaam) / location = lst (lat/lon)
    if len(location) == 2:
        link = f"http://api.openweathermap.org/data/2.5/forecast?lat={location[0]}&lon={location[1]}&appid={key}"
    else:
        link = f"http://api.openweathermap.org/geo/1.0/direct?q={location},NL&limit=1&appid={key}"
        response = requests.get(link)
        data = response.json()[0]
        lat = data["lat"]
        lon = data["lon"]
        link = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}"
    response = requests.get(link)
    weather = response.json()["list"]
    return weather
