from django.urls import path
from .views import SearchMusic,GetSong

urlpatterns = [
    path('search/', SearchMusic.as_view(), name='search'),
   
]
