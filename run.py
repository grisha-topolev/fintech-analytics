# run.py
"""
Запускает Flask-приложение для разработки.
"""
import os

from app import create_app


env: str = os.getenv("FLASK_ENV", "development")
app = create_app(env)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)