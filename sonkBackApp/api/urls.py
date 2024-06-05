from django.urls import path
from .views import *

urlpatterns = [
    path('search/', SearchMusic().as_view(), name='search'),
    path('searchByPage/', SearchMusicWithPage().as_view(), name='searchByPage'),
    path('artist/',GetArtist.as_view(),name='artist' ),
    path('song/',GetSong.as_view(),name='song'),
    path('getSuggestions/',GetSudggest.as_view(),name='suggestions'),
    path('top/',GetTopSongs.as_view(),name='topSongs'),
    path('playlist/top',GetPlaylistTop.as_view(),name='topPlaylist'),
    path('moodCategories',GetMoodCategories.as_view(),name='moodCategories'),
    path('autoComplete',GetAutoComplete.as_view(),name='autoComplete'),
    path('playlist',GetPlaylist.as_view(),name='playlist'),
    path('status',Status.as_view(),name='status'),
    path('posdcast',GetPosdscats.as_view(),name='podcast'),
    path('searchByMood',GetByMood.as_view(),name='searchByMood'),
]
