-- Включаем расширение columnar
CREATE EXTENSION IF NOT EXISTS citus_columnar;

-- Создаем таблицу в формате columnar
CREATE TABLE IF NOT EXISTS user_events (
    user_id UUID,
    event_name TEXT,
    platform TEXT,
    device TEXT,
    location TEXT,
    occurred_at TIMESTAMP
) USING columnar;

-- Делаем распределённой
SELECT create_distributed_table('user_events', 'user_id');