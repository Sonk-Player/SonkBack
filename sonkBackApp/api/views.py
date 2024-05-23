from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
import ytmusicapi

ytmusicapi = ytmusicapi.YTMusic()

# Create your views here.
class ShearchMusic(APIView):
    
    
    def get(self,request: Request):
        search = request.query_params
        name = search.get('name')
        data = ytmusicapi.search(name)
        return Response(data, status=status.HTTP_200_OK)
    
    