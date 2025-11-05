"""Сериализаторы для модели Movie."""

from rest_framework import serializers

from service.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Movie."""

    trailerLink = serializers.URLField(
        source="trailer_link",
        label="Ссылка на трейлер",
    )

    class Meta:
        """Метаданные сериализатора MovieSerializer."""

        model = Movie
        fields = (
            "id",
            "image",
            "trailerLink",
            "title",
            "duration",
        )
