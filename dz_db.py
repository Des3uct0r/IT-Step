import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time



def fetch_weather():
    URL = "https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BB%D1%8C%D0%B2%D1%96%D0%B2"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(URL, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        temperature_element = soup.find("p", class_="_6fYCPKSx")
        if temperature_element:
            temperature = temperature_element.text.strip()
            return temperature
        else:
            return None
    except Exception as e:
        return None


def main():
    with sqlite3.connect('w.sl3', timeout=10) as connect:
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS weather (datetime TEXT, temperature TEXT);")
        connect.commit()

        while True:
            temperature = fetch_weather()
            if temperature:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
                cursor.execute("INSERT INTO weather (datetime, temperature) VALUES (?, ?);",
                               (current_time, temperature))
                connect.commit()

            cursor.execute("SELECT rowid, datetime, temperature FROM weather;")
            data = cursor.fetchall()
            print("Stored data:", data)

            time.sleep(1800)


if __name__ == "__main__":
    main()
