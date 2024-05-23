from django.urls import path
from .views import SearchMusic,GetArtist

urlpatterns = [
    path('search/', SearchMusic.as_view(), name='search'),
    path('artist/',GetArtist.as_view(),name='artist' )
]
