from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
import ytmusicapi
from .filterCategory import  filterCategory
from pytube import YouTube
from .mappers import mapperSong
from urllib.parse import unquote
from ytmusicapi.parsers._utils import (nav, NAVIGATION_BROWSE_ID, SECTION_LIST, SINGLE_COLUMN_TAB, TITLE_TEXT, GRID_ITEMS,CATEGORY_PARAMS,CAROUSEL_CONTENTS)
from ytmusicapi.parsers.browsing import parse_playlist, parse_content_list

ytmusicapi = ytmusicapi.YTMusic()

# Create your views here.
#Path: search?name=????
class SearchMusic(APIView):
    
    def get(self,request: Request):
        
        search = request.query_params
        print(search)
        query = search.get('query')
       
        filters = search.get('filter')

        try: 
            if(filterCategory.verfiyFilters(filters)==True):
            
                data = ytmusicapi.search(query=query, filter=filters)
            else:
                data = ytmusicapi.search(query=query) 

                
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
class SearchMusicWithPage(APIView):
    
    
    def get(self,request: Request):
        
        search = request.query_params
        print(search)
        query = search.get('query')
        page = search.get('page')
        filters = search.get('filter')

        print(filterCategory.verfiyFilters(filters))
        try: 
            if(filterCategory.verfiyFilters(filters)==True):
                print(filters)
                data = ytmusicapi.search(query=query+'&' + page, filter=filters)
            else:
                data = ytmusicapi.search(query=query +'&' + page) 

                
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetArtist(APIView):
    
    def get(self,request: Request):
        
        search = request.query_params
        chanelId = unquote(search.get('chanelId'))
        try:
           
            data = ytmusicapi.get_artist(channelId=chanelId)
         
           
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class GetSong(APIView):
    
    
    def get(self,request: Request):
        
        search = request.query_params
        print(search)
        songId = search.get('songId')
        print(songId)
        
        try: 
            data = ytmusicapi.get_song(songId)

            data = mapperSong(data) 


            return Response(data, status=status.HTTP_200_OK, content_type='application/json')
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        

# Path: getSuggestions?songId=????
class GetSudggest(APIView):
    def get(self,request: Request):
        search = request.query_params
        name = search.get('name')
        songId = search.get('songId')
      
        try:             
            
            data  = ytmusicapi.search(name,filter='songs')      
            
            newData = []
            for i in range(len(data)):  
                if data[i]["videoId"] != songId:
                    newData.append(data[i])

            return Response(newData, status=status.HTTP_200_OK)
        except Exception as e:            
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Path: top?limit=????
class GetTopSongs(APIView):
    def get(self,request: Request):
        search = request.query_params
        print(search)
        limit = search.get('limit')
        try: 
            if(limit == None):
                data = ytmusicapi.search(query='top songs', filter='songs', limit=50)
            else:
                data = ytmusicapi.search(query='top songs', filter='songs', limit=int(limit))

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        


class GetPlaylistTop(APIView):
    def get(self,request: Request):
        search = request.query_params
        playlistId = search.get('playlistId')
        try: 
            data = ytmusicapi.get_search_suggestions(query='Top mundial', filter='playlists', limit=100)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class GetMoodCategories(APIView):
    
    def get(self,request: Request):
        try:
            data = ytmusicapi.get_mood_categories()
            return Response(data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
class GetAutoComplete(APIView):
    
    def get(self,request: Request):
        search = request.query_params
        query = search.get('query')
        try:
            data = ytmusicapi.get_search_suggestions(query)
            return Response(data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
class GetPlaylist(APIView):
    
    def get(self,request: Request):
        search = request.query_params
        browseId = search.get('browseId')
        try:
            data = ytmusicapi.get_playlist(browseId)
            return Response(data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
class Status(APIView):
    
    def get(self,request: Request):
        try:
            
            return Response('ok', status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
class GetPosdscats(APIView):
        
        def get(self,request: Request):
            
            search = request.query_params
            query = search.get('query')
            try:
                data = ytmusicapi.search(query='podcasts' , filter='podcasts')
                newData=[]
                for item in data:
                    if item["resultType"] == 'podcast':
                        newData.append(item)    

                return Response(newData, status=status.HTTP_200_OK)
            
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
class GetByMood(APIView):
    def get(self,request: Request):
        search = request.query_params
        mood = search.get('mood')
        try:
            
            # data = ytmusicapi.get_mood_playlists(params=mood)
            playlists = []
            respose = ytmusicapi._send_request("browse", {"browseId": "FEmusic_moods_and_genres_category", "params": mood})
            
            for section in nav(respose, SINGLE_COLUMN_TAB + SECTION_LIST):
                try:
                    path = []
                    
                    if "gridRenderer" in section:
                        path = GRID_ITEMS
                    elif "musicCarouselShelfRenderer" in section:
                        path = CAROUSEL_CONTENTS
                    elif "musicImmersiveCarouselShelfRenderer" in section:
                        path = ["musicImmersiveCarouselShelfRenderer", "contents"]
                    if len(path):
                        results = nav(section, path)
                        playlists += parse_content_list(results, parse_playlist)
                except Exception as e:
                    print(e)
                    pass


            return Response(playlists, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class GetAlbum(APIView):
    def get(self,request: Request):
        search = request.query_params
        albumId = search.get('albumId')
        try:
            data = ytmusicapi.get_album(albumId)
            return Response(data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

