"""Маршруты проекта Movies."""

from django.conf import settings
from django.conf.urls.static import static as static_serve
from django.contrib import admin
from django.templatetags.static import static as static_url
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("", include("api.urls")),
    path("admin/", admin.site.urls),
    path(
        "favicon.ico",
        RedirectView.as_view(
            url=static_url("favicon.ico"),
            permanent=True,
        ),
    ),
]

if settings.DEBUG:
    urlpatterns += static_serve(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
