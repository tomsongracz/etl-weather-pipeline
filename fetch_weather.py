import requests
import pandas as pd

# Lista miast wraz z ich współrzędnymi geograficznymi
CITIES = {
    "Warszawa": (52.2297, 21.0122),
    "Gdańsk": (54.3520, 18.6466),
    "Sitaniec": (50.7333, 23.2833),
    "Hrubieszów": (50.8050, 23.8925),
    "Portimao": (37.1366, -8.5392),
    "Morro Jable": (28.1800, -14.1000),
}

# Adres API do pobierania prognozy pogody
API_URL = "https://api.open-meteo.com/v1/forecast"


def fetch_weather():
    # Lista do przechowywania danych pogodowych dla wszystkich miast
    all_data = []

    # Iteracja po wszystkich miastach i ich współrzędnych
    for city, (lat, lon) in CITIES.items():
        # Parametry zapytania do API (współrzędne i żądanie bieżącej pogody)
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True,
        }
        # Wysyłamy żądanie HTTP GET do API
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # jeśli błąd, rzuci wyjątek
        data = response.json()  # odpowiedź w formacie JSON

        # Sprawdzamy, czy w odpowiedzi znajduje się sekcja "current_weather"
        if "current_weather" in data:
            weather = data["current_weather"]
            weather["city"] = city  # dodajemy nazwę miasta do danych
            all_data.append(weather)  # dopisujemy dane do listy

    # Tworzymy DataFrame pandas z zebranych danych
    df = pd.DataFrame(all_data)
    return df


if __name__ == "__main__":
    # Pobieramy dane pogodowe
    df = fetch_weather()
    # Wyświetlamy wynik
    print(df)

