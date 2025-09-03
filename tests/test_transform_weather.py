import pandas as pd
from transform_weather import transform_weather


def test_transform_weather_changes_columns():
    # Tworzymy przykładowy DataFrame z minimalnymi danymi wejściowymi
    sample = pd.DataFrame(
        [{
            "temperature": 20,
            "windspeed": 5,
            "winddirection": 180,
            "time": "2025-01-01T12:00",
            "city": "Warszawa",
            "weathercode": 2,
        }]
    )

    # Przetwarzamy dane za pomocą funkcji transform_weather
    df = transform_weather(sample)

    # Sprawdzamy, czy kolumny zostały zmienione i dodane
    assert "temp_celsius" in df.columns
    assert "weather_desc" in df.columns

    # Sprawdzamy, czy kolumna timestamp ma typ datetime
    assert pd.api.types.is_datetime64_any_dtype(df["timestamp"])

    # Sprawdzamy, czy opis pogody odpowiada kodowi 2 ("Częściowe zachmurzenie")
    assert df.loc[0, "weather_desc"] == "Częściowe zachmurzenie"
