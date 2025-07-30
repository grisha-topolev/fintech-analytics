#!/bin/sh

export PYTHONPATH=/app

# Ожидание готовности базы данных
echo "Ждём базу данных..."

RETRIES=10
until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" || [ $RETRIES -eq 0 ]; do
  echo "Ожидаем PostgreSQL... осталось попыток: $RETRIES"
  RETRIES=$((RETRIES - 1))
  sleep 2
done

if [ $RETRIES -eq 0 ]; then
  echo "❌ PostgreSQL не доступен. Завершение."
  exit 1
fi

echo "✅ PostgreSQL готов. Запускаем инициализацию..."

# Запуск инициализации базы
python -m app.init_db

echo "🚀 Запускаем Flask API..."
exec gunicorn "app:create_app()" --bind 0.0.0.0:5050 --worker-class sync --workers 2