# app/db.py
import os

import psycopg
from psycopg import Connection
from dotenv import load_dotenv


# Загружаем переменные окружения из .env
load_dotenv()

def get_connection() -> Connection:
    """
    Создает и возвращает подключение к PostgreSQL.
    """
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )