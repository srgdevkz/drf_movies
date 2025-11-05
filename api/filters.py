"""Фильтры для модели Movie."""

from django_filters import rest_framework as filters
from django_filters.rest_framework import FilterSet

from service.models import Movie


class MovieFilter(FilterSet):
    """Фильтр для фильтрации фильмов по названию."""

    title = filters.CharFilter(lookup_expr="startswith")

    class Meta:
        """Метаданные фильтра MovieFilter."""

        model = Movie
        fields = ("title",)
