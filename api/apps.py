"""Конфигурация приложения api."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """AppConfig для API."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
    verbose_name = "API"
