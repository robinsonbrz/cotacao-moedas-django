from django.urls import path

from .views import PrecosAPIView

app_name = 'apimoedas'

urlpatterns = [
    path('precos/', PrecosAPIView.as_view(), name='precos'),
]
