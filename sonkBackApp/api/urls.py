from django.urls import path
from .views import SearchMusic,GetArtist,GetSong,GetSudggest,GetTopSongs,GetPlaylistTop,SearchMusicWithPage

urlpatterns = [
    path('search/', SearchMusic().as_view(), name='search'),
    path('searchByPage/', SearchMusicWithPage().as_view(), name='searchByPage'),
    path('artist/',GetArtist.as_view(),name='artist' ),
    path('song/',GetSong.as_view(),name='song'),
    path('getSuggestions/',GetSudggest.as_view(),name='suggestions'),
    path('top/',GetTopSongs.as_view(),name='topSongs'),
    path('playlist/top',GetPlaylistTop.as_view(),name='topPlaylist')
]
