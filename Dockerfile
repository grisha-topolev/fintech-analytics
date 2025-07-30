# Используем официальный минимальный образ Python
FROM python:3.11-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y build-essential libpq-dev postgresql-client && rm -rf /var/lib/apt/lists/*

# Создаем рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Добавляем переменную окружения
ENV PYTHONPATH=/app

# Делаем entrypoint.sh исполняемым
RUN chmod +x entrypoint.sh

# Открываем порт
EXPOSE 5050

# Запуск через entrypoint
CMD ["sh", "./entrypoint.sh"]