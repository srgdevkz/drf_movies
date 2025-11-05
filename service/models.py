"""Модели сервиса фильмов."""

from django.core.validators import MinValueValidator
from django.db import models

from movies.constants import (
    ONE,
    POSTER_UPLOAD_TO,
    TITLE_MAX_LENGTH,
    URL_MAX_LENGTH,
)


class Movie(models.Model):
    """Фильм."""

    image = models.ImageField(
        verbose_name="Изображение",
        upload_to=POSTER_UPLOAD_TO,
        blank=True,
    )
    trailer_link = models.URLField(
        verbose_name="Ссылка на трейлер",
        max_length=URL_MAX_LENGTH,
    )
    title = models.CharField(
        verbose_name="Название",
        max_length=TITLE_MAX_LENGTH,
    )
    duration = models.PositiveIntegerField(
        verbose_name="Длительность в минутах",
        validators=[
            MinValueValidator(ONE),
        ],
        blank=True,
        null=True,
    )

    class Meta:
        """Метаданные модели Movie."""

        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}"
