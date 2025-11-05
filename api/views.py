"""Представления (views) для работы с фильмами в API."""

from django.http import Http404
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets
from rest_framework.exceptions import NotFound

from service.models import Movie

from .filters import MovieFilter
from .serializers import MovieSerializer


def home_view(request):
    """Отображает главную страницу приложения API."""
    template = "api/home.html"
    context = {}
    return render(request, template, context)


class MovieViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Movie с фильтрацией и поиском."""

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = MovieFilter
    search_fields = ("title",)
    ordering_fields = ("id", "title")
    ordering = ("id",)

    def get_object(self):
        """Возвращает объект Movie или ошибку, если не найден."""
        try:
            return super().get_object()
        except Http404 as e:
            raise NotFound(
                _("Фильм с указанным идентификатором не найден."),
            ) from e
