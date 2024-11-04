# cities/urls.py
from django.urls import path
from .views import CityListView

urlpatterns = [
    path('api/cities/', CityListView.as_view(), name='city-list'),
]

