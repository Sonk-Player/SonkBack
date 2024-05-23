from django.urls import path
from .views import ShearchMusic

urlpatterns = [
    path('search/', ShearchMusic.as_view(), name='search'),
]
