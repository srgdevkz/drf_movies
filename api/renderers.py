"""Рендерер JSON с кодировкой UTF-8."""

from rest_framework.renderers import JSONRenderer


class UTF8JSONRenderer(JSONRenderer):
    """Рендерер для вывода JSON с кодировкой UTF-8."""

    edia_type = "application/json"
    charset = "utf-8"
