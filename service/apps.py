"""Конфигурация приложения service."""

from django.apps import AppConfig


class ServiceConfig(AppConfig):
    """AppConfig для сервиса фильмов."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "service"
    verbose_name = "Сервис"
