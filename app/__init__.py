# app/__init__.py
"""
Фабрика приложения Flask.
"""
import os

from flask import Flask

from app.config import get_config


def create_app(env: str = None) -> Flask:
    """
    Создаёт и настраивает экземпляр Flask-приложения.
    :param env: Название окружения (development / production)
    """
    env = env or os.getenv("FLASK_ENV", "development")
    config_class = get_config(env)

    app = Flask(__name__)
    app.config.from_object(config_class)

    # Импорт и регистрация роутов
    from app.app import register_routes
    register_routes(app)

    return app