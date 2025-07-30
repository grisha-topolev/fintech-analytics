# app/config.py
"""
Конфигурации Flask-приложения по окружениям.
"""
from typing import Type


class BaseConfig:
    """Базовая конфигурация, общая для всех окружений."""
    DB_HOST: str = "coordinator"
    DB_PORT: int = 5432
    DB_NAME: str = "postgres"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DEBUG: bool = False
    TESTING: bool = False


class DevelopmentConfig(BaseConfig):
    """Конфигурация для разработки."""
    DEBUG: bool = True


class ProductionConfig(BaseConfig):
    """Конфигурация для продакшена."""
    DEBUG: bool = False


def get_config(env: str) -> Type[BaseConfig]:
    """Выбор нужной конфигурации по окружению."""
    if env == "production":
        return ProductionConfig
    return DevelopmentConfig