import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from transform_weather import transform_weather
from fetch_weather import fetch_weather

# Wczytujemy zmienne z pliku .env
load_dotenv()

# Składamy URL połączenia do PostgreSQL
DB_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)


def load_weather(df: pd.DataFrame):
    """
    Funkcja ładuje DataFrame do tabeli 'weather' w PostgreSQL.
    """
    engine = create_engine(DB_URL)
    df.to_sql("weather", engine, if_exists="append", index=False)
    print("Dane zostały zapisane do PostgreSQL!")


if __name__ == "__main__":
    # Pobranie danych
    df = fetch_weather()
    # Transformacja danych
    df = transform_weather(df)
    # Zapis do bazy
    load_weather(df)
