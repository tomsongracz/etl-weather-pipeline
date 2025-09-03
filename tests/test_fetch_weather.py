from fetch_weather import fetch_weather
import pandas as pd


def test_fetch_weather_returns_dataframe():
    # Pobieramy dane pogodowe za pomocą funkcji fetch_weather
    df = fetch_weather()

    # Sprawdzamy, czy zwrócony obiekt to DataFrame pandas
    assert isinstance(df, pd.DataFrame)

    # Sprawdzamy, czy DataFrame nie jest pusty
    assert not df.empty


def test_dataframe_contains_expected_columns():
    df = fetch_weather()
    # Oczekiwane kolumny zgodne z API + dodana kolumna "city"
    expected_columns = {
        "temperature",
        "windspeed",
        "winddirection",
        "weathercode",
        "time",
        "city",
    }
    assert expected_columns.issubset(df.columns)


def test_city_column_contains_expected_cities():
    df = fetch_weather()
    expected_cities = {
        "Warszawa",
        "Gdańsk",
        "Sitaniec",
        "Hrubieszów",
        "Portimao",
        "Morro Jable",
    }
    assert set(df["city"]).issubset(expected_cities)


def test_temperature_column_is_numeric():
    df = fetch_weather()
    # Sprawdzamy, czy kolumna temperature zawiera liczby
    assert pd.api.types.is_numeric_dtype(df["temperature"])


def test_windspeed_column_is_numeric():
    df = fetch_weather()
    # Sprawdzamy, czy kolumna windspeed zawiera liczby
    assert pd.api.types.is_numeric_dtype(df["windspeed"])
