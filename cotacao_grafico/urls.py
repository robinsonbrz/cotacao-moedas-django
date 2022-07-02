# criar urls.py pasta do app
from django.urls import path

from . import views

app_name = 'cotacao_grafico'

urlpatterns = [
    path('', views.home, name='home'),
]
