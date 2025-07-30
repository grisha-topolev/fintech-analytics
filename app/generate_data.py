# app/generate_data.py
import uuid
import random
from datetime import datetime
from typing import List, Tuple

from faker import Faker

from app.db import get_connection


fake = Faker()

def generate_events(n: int = 10_000) -> None:
    """
    Генерирует и вставляет n событий пользователей в таблицу user_events.
    """

    # Подготовка списка записей
    events: List[Tuple[uuid.UUID, str, str, str, str, datetime]] = [
        (
            uuid.uuid4(),  # user_id
            random.choice(['login', 'payment', 'transfer', 'logout']),
            random.choice(['iOS', 'Android', 'Web']),
            fake.user_agent(),      # device
            fake.country(),         # location
            fake.date_time_between(start_date='-30d', end_date='now')  # occurred_at
        )
        for _ in range(n)
    ]

    # Вставка в базу
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.executemany(
                """
                INSERT INTO user_events (
                    user_id, event_name, platform, device, location, occurred_at
                ) VALUES (%s, %s, %s, %s, %s, %s)
                """,
                events
            )
        conn.commit()

    print(f"✅ Inserted {n} events.")

if __name__ == "__main__":
    generate_events()