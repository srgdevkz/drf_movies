"""Маршруты приложения API для фильмов."""

from django.urls import include, path
from rest_framework import routers

from .views import MovieViewSet, home_view

app_name = "api"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("", home_view),
    path("", include(router.urls)),
]
