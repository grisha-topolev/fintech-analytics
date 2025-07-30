# app/init_db.py
from app.db import get_connection


def init_db():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS user_events (
                    user_id UUID,
                    event_name TEXT,
                    platform TEXT,
                    device TEXT,
                    location TEXT,
                    occurred_at TIMESTAMP
                );
            """)
            # Создаем distributed table, если она ещё не создана
            try:
                cur.execute("SELECT create_distributed_table('user_events', 'user_id');")
            except Exception as e:
                print(f"⚠️ Возможно, таблица уже распределена: {e}")
        conn.commit()
    print("✅ Инициализация завершена")


if __name__ == "__main__":
    init_db()