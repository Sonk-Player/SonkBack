from django.urls import path
from .views import SearchMusic

urlpatterns = [
    path('search/', SearchMusic.as_view(), name='search'),
]
