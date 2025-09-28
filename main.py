from services.open_weather import fetch_weather
from services.exel_file import create
from services.mysql_db import save_weather
import time


#1. pobieranie danych podogowych
weather = fetch_weather()

#2. Zapisanie danych do pliku
create(weather, "data/file.xlsx")

while True:
    # 1. pobieranie danych podogowych
    weather = fetch_weather()

    # 2. Zapisanie danych do pliku
    create(weather, "data/file.xlsx")

    save_weather(weather)

    time.sleep(10)
    print("Pobrano dane pogodowe")