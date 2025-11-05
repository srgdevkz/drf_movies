"""Настройки панели администратора для модели Movie."""

from django.contrib import admin
from django.utils.html import mark_safe
from import_export.admin import ImportExportModelAdmin
from import_export.formats.base_formats import CSV

from .models import Movie


class TitleFilter(admin.SimpleListFilter):
    """Фильтр фильмов по названию (в порядке добавления)."""

    title = "Название"
    parameter_name = "title"

    def lookups(self, request, model_admin):
        movies = Movie.objects.all().order_by("id")
        return [(m.title, m.title) for m in movies]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title=self.value())
        return queryset


@admin.register(Movie)
class MovieAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """Админ-панель для управления фильмами."""

    formats = [CSV]
    list_display = (
        "id",
        "image_preview",
        "trailer_link",
        "title",
        "duration",
    )
    list_display_links = ("title",)
    list_filter = (TitleFilter,)
    search_fields = ("title",)
    search_help_text = "Название для поиска."
    ordering = ["id"]

    fieldsets = (
        (
            "Основное",
            {
                "fields": ("title", "duration"),
            },
        ),
        (
            "Медиа",
            {
                "fields": ("image", "trailer_link"),
            },
        ),
    )

    @admin.display(description="Изображение")
    def image_preview(self, obj):
        """Отображает превью изображения фильма в админке."""
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="40" height="40" '
                f'style="object-fit:cover; border-radius: 4px;" />'
            )
        return "Нет изображения"
