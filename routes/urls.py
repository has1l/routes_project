from django.urls import path
from . import views  # Импортируем файл views.py

urlpatterns = [
    path("", views.home, name="home"),  # Маршрут для главной страницы
]
