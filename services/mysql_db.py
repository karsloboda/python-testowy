import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"), # lub 127.0.0.1
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if connection.is_connected():
            print("Połączono z bazą")
            return connection

    except:
        print("błąd")
        return None


def save_weather(data):
    try:
       conn = create_connection()
       cursor = conn.cursor()
       query = """
       INSERT INTO odczyty
       (temperatura,odczuwalna,opis,wiatr,wilgotnosc,miejsce,czas)
       VALUES (%s, %s, %s, %s, %s, %s, %s)
       """
       values = (
           data["temperature"],
           data["feels_like"],
           data["description"],
           data["wind_speed"],
           data["humidity"],
           data["place"],
           data["timestamp"]
       )

       cursor.execute(query, values)
       conn.commit()
       conn.close()
       print("Zapisano odczyt do bazy")


    except Exception as e:
        print(e)


def read_all(connection):
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM odczyty"
    cursor.execute(query)
    results = cursor.fetchall()

    print(results)





