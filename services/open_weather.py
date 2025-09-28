import requests
from datetime import datetime
from utils.tools import convert_temp, convert_wind

def fetch_weather():
    city = "Lisbon"
    api_key = "11506fd61f40da2b23a58fbcf814afbd"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    # weather = {
    #     # temperatura
    #     "temperatue": data["main"]["temp"],
    #     # temp. odczuwalna
    #     "feel": data["main"]["feels_like"],
    #     # opis pogody (description)
    #     "description": data["weather"][0]["description"],
    #     # prędkośc wiatru
    #     "wind": data["wind"]["speed"],
    #     # wilgotność
    #     "humidity": data["main"]["humidity"],
    #     # miejsce
    #     "place": data["sys"]["country"][0],
    #     # godzina (nie z API tylko z datetime)
    #     "time": datetime.datetime.now().strftime("%I:%M %p")
    # }

    weather = {
        "temperature": convert_temp(data.get("main").get("temp"), "C"),
        "feels_like": convert_temp(data.get("main").get("feels_like"), "C"),
        "description": data.get("weather")[0].get("description"),
        "wind_speed": convert_wind(data.get("wind").get("speed"), "KM"),
        "humidity": data.get("main").get("humidity"),
        "place": data.get("name"),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return weather

