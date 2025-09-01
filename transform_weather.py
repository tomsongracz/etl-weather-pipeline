import pandas as pd

# Słownik kodów pogodowych -> opis w języku polskim
WEATHER_CODES = {
    0: "Czyste niebo",
    1: "Przeważnie bezchmurnie",
    2: "Częściowe zachmurzenie",
    3: "Zachmurzenie",
    45: "Mgła",
    48: "Mgła osadzająca szron",
    51: "Mżawka lekka",
    53: "Mżawka umiarkowana",
    55: "Mżawka intensywna",
    56: "Marznąca mżawka lekka",
    57: "Marznąca mżawka gęsta",
    61: "Deszcz lekki",
    63: "Deszcz umiarkowany",
    65: "Deszcz intensywny",
    66: "Marznący deszcz lekki",
    67: "Marznący deszcz silny",
    71: "Śnieg lekki",
    73: "Śnieg umiarkowany",
    75: "Śnieg intensywny",
    77: "Śnieg ziarnisty",
    80: "Przelotne opady deszczu lekkie",
    81: "Przelotne opady deszczu umiarkowane",
    82: "Przelotne opady deszczu intensywne",
    85: "Przelotne opady śniegu lekkie",
    86: "Przelotne opady śniegu intensywne",
    95: "Burza (lekka/umiarkowana)",
    96: "Burza z lekkim gradem",
    99: "Burza z silnym gradem",
}


def transform_weather(df: pd.DataFrame) -> pd.DataFrame:
    """
    Walidacja, czyszczenie i dodanie opisu warunków pogodowych.
    """
    # Zmieniamy nazwy kolumn na bardziej czytelne
    df = df.rename(
        columns={
            "temperature": "temp_celsius",
            "windspeed": "wind_speed",
            "winddirection": "wind_dir",
            "time": "timestamp",
        }
    )

    # Konwertujemy typy danych
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["temp_celsius"] = df["temp_celsius"].astype(float)
    df["wind_speed"] = df["wind_speed"].astype(float)

    # Usuwamy duplikaty (dla tego samego miasta i czasu)
    df = df.drop_duplicates(subset=["city", "timestamp"])

    # Dodajemy opis pogody na podstawie kodu
    df["weather_desc"] = df["weathercode"].map(WEATHER_CODES)

    return df


if __name__ == "__main__":
    # Importujemy funkcję do pobrania danych pogodowych
    from fetch_weather import fetch_weather

    # Pobieramy dane pogodowe
    df = fetch_weather()

    # Przetwarzamy dane
    df = transform_weather(df)

    # Wyświetlamy wynik
    print(df)
