from django.urls import path
from . import views

urlpatterns = [
    path('recibidos/', views.mensajes_recibidos, name='mensajes_recibidos'),
]
