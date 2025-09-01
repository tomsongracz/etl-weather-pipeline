# test_load_weather.py
import os
import pandas as pd
import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect, text
from load_weather import load_weather

# Wczytanie zmiennych środowiskowych z .env
load_dotenv()

DB_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@{os.getenv('POSTGRES_HOST', 'localhost')}:{os.getenv('POSTGRES_PORT', '5432')}"
    f"/{os.getenv('POSTGRES_DB')}"
)


@pytest.fixture
def engine():
    """Tworzy połączenie do bazy danych PostgreSQL"""
    return create_engine(DB_URL)


def test_load_weather_to_postgres(engine):
    """Test ładowania danych do tabeli weather w PostgreSQL"""

    # Tworzymy przykładowy DataFrame
    df = pd.DataFrame(
        [
            {
                "temp_celsius": 20,
                "wind_speed": 5,
                "wind_dir": 180,
                "timestamp": pd.Timestamp("2025-01-01 12:00"),
                "city": "Warszawa",
                "weathercode": 2,
                "weather_desc": "Częściowe zachmurzenie",
            }
        ]
    )

    # Ładujemy dane do bazy danych
    load_weather(df)

    # Sprawdzamy, czy tabela weather istnieje
    inspector = inspect(engine)
    assert "weather" in inspector.get_table_names()

    # Sprawdzamy, czy tabela zawiera jakieś rekordy
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM weather"))
        count = result.scalar()
        assert count > 0
