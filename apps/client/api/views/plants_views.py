from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.client.api.views.requests.plants_requests import list_plants ,detail_plant
from rest_framework.decorators import api_view


# plants list
@api_view(['GET'])
def list_plants_api_view(request):
    
    
    if request.method == 'GET':
        plants,status_code = list_plants()
        if status_code == 200:
            return Response(plants, status= status.HTTP_200_OK)
        else:
            return Response(plants,status=status.HTTP_404_NOT_FOUND)
        
        
# plant detail 
@api_view(['GET'])
def view_plant_api_view(request,pk=None):
    
    
    if request.method == 'GET':
        plant,status_code = detail_plant(pk)
        if status_code == 200:
            return Response(plant, status= status.HTTP_200_OK)
        else:
            return Response(plant,status=status.HTTP_404_NOT_FOUND)