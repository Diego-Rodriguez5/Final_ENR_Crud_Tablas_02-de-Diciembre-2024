from django.urls import path
from app_base import views

urlpatterns = [
        #inicio Pupi Pet - Mascotas
    path('', views.inicio),
]