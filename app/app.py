# app/app.py

from typing import List, Tuple

from psycopg import Cursor
from flask import Flask, jsonify

from app.db import get_connection


def register_routes(app: Flask) -> None:
    """
    Регистрирует все маршруты API на переданном экземпляре Flask.
    """
    @app.route("/api/summary/events")
    def total_events() -> str:
        """Возвращает общее количество событий."""
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur: Cursor
                cur.execute("SELECT COUNT(*) FROM user_events")
                total: int = cur.fetchone()[0]
        return jsonify({"total_events": total})


    @app.route("/api/summary/daily")
    def daily_stats() -> str:
        """Возвращает количество событий по дням."""
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur: Cursor
                cur.execute("""
                    SELECT occurred_at::date, COUNT(*)
                    FROM user_events
                    GROUP BY occurred_at::date
                    ORDER BY occurred_at::date DESC
                """)
                results: List[Tuple[str, int]] = cur.fetchall()
        return jsonify([{"date": str(row[0]), "count": row[1]} for row in results])


    @app.route("/api/summary/platforms")
    def platform_stats() -> str:
        """Возвращает количество событий по платформам."""
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur: Cursor
                cur.execute("""
                    SELECT platform, COUNT(*)
                    FROM user_events
                    GROUP BY platform
                """)
                results: List[Tuple[str, int]] = cur.fetchall()
        return jsonify([{"platform": row[0], "count": row[1]} for row in results])


    @app.route("/api/summary/locations")
    def location_stats() -> str:
        """Возвращает количество событий по локациям."""
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur: Cursor
                cur.execute("""
                    SELECT location, COUNT(*)
                    FROM user_events
                    GROUP BY location
                """)
                results: List[Tuple[str, int]] = cur.fetchall()
        return jsonify([{"location": row[0], "count": row[1]} for row in results])