import requests
import json

def wheather_in_bergen_next_hour():
    url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.381463&lon=5.331609"
    header = {"User-Agent": "inf100.ii.uib.no nosor6106"}
    webpage = requests.get(url, headers=header)
    weather_dict = json.loads(webpage.content.decode("utf-8"))
    weather = (weather_dict["properties"]["timeseries"][00]["data"]["next_1_hours"]["summary"]["symbol_code"])
    return weather

print("Været i Bergen neste time:", wheather_in_bergen_next_hour())