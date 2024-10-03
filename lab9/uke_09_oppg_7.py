def weather_report(weather_stations, city):
    weather = weather_stations[city]
    if city in weather_stations:
        print("The weather in", city, end="")
        print(": \nThe wind speed is", weather["Wind speed"], end="")
        print("m/s in the", weather["Wind direction"], "direction and the precipitation is", weather["Precipitation"], end="")
        print("mm. \nThe measurement was done using the", weather["Device"], "weather station.")

weather_stations = {
    "Bergen": {
        "Wind speed": 3.6,
        "Wind direction": "northeast",
        "Precipitation": 5.2,
        "Device": "WeatherMaster500"
    },
    "Trondheim": {
        "Wind speed": 8.2,
        "Wind direction": "northwest",
        "Precipitation": 0.2,
        "Device": "ClimateDiscoverer3000"
    },
    "Svalbard": {
        "Wind speed": 7.5,
        "Wind direction": "southwest",
        "Precipitation": 1.1,
        "Device": "WeatherFinder5.0"
    },
}

weather_report(weather_stations, "Bergen")