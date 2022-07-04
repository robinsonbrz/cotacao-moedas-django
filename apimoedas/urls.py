from django.urls import path

from .views import PrecosAPIView

urlpatterns = [
    path('precos/', PrecosAPIView.as_view(), name='precos'),
]
