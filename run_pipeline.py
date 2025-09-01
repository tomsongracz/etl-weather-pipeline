"""
Ten plik uruchamia cały pipeline ETL w jednym kroku:
1. Pobranie danych pogodowych (Extract)
2. Transformacja i walidacja danych (Transform)
3. Zapis do PostgreSQL (Load)
"""

from fetch_weather import fetch_weather
from transform_weather import transform_weather
from load_weather import load_weather


def run_pipeline():
    print("Pobieranie danych pogodowych...")
    df = fetch_weather()

    print("Transformacja danych...")
    df = transform_weather(df)

    print("Zapis do PostgreSQL...")
    load_weather(df)

    print("Pipeline zakończony sukcesem!")


if __name__ == "__main__":
    run_pipeline()
