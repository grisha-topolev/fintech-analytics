# 📊 Fintech Analytics

Flask-приложение для аналитики пользовательских событий в финтех-среде с использованием **PostgreSQL + Citus Columnar**, контейнеризации через **Docker Compose**, и автогенерацией данных.

---

## 🚀 Возможности

- API для получения аналитики:
  - Общее количество событий
  - События по дням
  - События по платформам
  - События по локациям
- Горизонтально масштабируемая БД через [Citus](https://www.citusdata.com/)
- Быстрое чтение аналитики благодаря [Citus Columnar](https://www.citusdata.com/blog/2022/04/12/columnar-compression-for-analytics-on-postgres/)
- Поддержка генерации тестовых событий (`faker`)
- Разделение конфигураций по окружениям (dev/prod)
- Логирование
- REST API
- Gunicorn

---

## 🧱 Стек технологий

- 🐍 Python 3.11 + Flask
- 🐘 PostgreSQL + Citus + Citus Columnar
- 🐳 Docker + Docker Compose
- 🧪 Pytest (опционально)
- 📦 SQLAlchemy (по желанию, пока не используется)

---

## ⚙️ Установка и запуск

### 1. Клонируй репозиторий

```bash
git clone https://github.com/your-username/fintech-analytics.git
cd fintech-analytics
```

### 2. Убедись, что установлен Docker и Docker Compose

### 3. Запусти все

```bash
docker compose up --build
```

### 4. Проверка

Открой в браузере:
	•	http://localhost:5050/api/summary/events

---

## Генерация данных

```bash
docker compose exec api python -m app.generate_data
```

---

## 🧠 Почему Citus Columnar?
	•	Горизонтальное масштабирование — данные распределяются по worker-нодам
	•	Колонночное хранение — идеальное решение для аналитики (читаем только нужные столбцы)
	•	Сжатие данных — экономия места и более быстрая аналитика
	•	PostgreSQL API — можно использовать обычные SELECT-запросы

---

## 🛠 Переменные окружения (.env)

```env
DB_HOST=coordinator
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
FLASK_ENV=development
```

---

## 📌 TODO / Планы
	•	Подключить SQLAlchemy
	•	Добавить покрытие тестами
	•	Добавить метрики (Prometheus + Grafana)
	•	Авторизация по токену
	•	Выгрузка аналитики в CSV
