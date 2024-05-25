from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
import ytmusicapi
from .filterCategory import  filterCategory
from pytube import YouTube
from .mappers import mapperSong
from urllib.parse import unquote
ytmusicapi = ytmusicapi.YTMusic()

# Create your views here.
#Path: search?name=????
class SearchMusic(APIView):
    
    
    def get(self,request: Request):
        
        search = request.query_params
        print(search)
        name = search.get('name')
        limit = search.get('limit')
       
        filters = search.get('filter')

        print(filterCategory.verfiyFilters(filters))
        try: 
            if(filterCategory.verfiyFilters(filters)==True):
                print(filters)
                data = ytmusicapi.search(query=name, filter=filters)
            else:
                data = ytmusicapi.search(name)  
                
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetArtist(APIView):
    
    def get(self,request: Request):
        
        search = request.query_params
        print(search)
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
        songId = unquote(search.get('songId')) 
        
        
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
        songId = unquote(search.get('songId')) 
        print(name)
        print(songId)
        try:             
            
            data  = ytmusicapi.search(name,filter='songs', limit=5)      

            newData = []
            for i in range(len(data)):  
                if data[i]["videoId"] != songId:
                    newData.append(data[i])

            return Response(newData, status=status.HTTP_200_OK)
        except Exception as e:            
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    