from rest_framework.decorators import api_view

from apps.client.api.serializers.client_serializers import List_ClientSerializer, Create_ClientSerializer
from rest_framework.response import Response
from rest_framework import status

from apps.client.models import User



        
@api_view(['GET'])
def list_client_api_view(request):
    
    # list
    if request.method == 'GET':
        user = User.objects.all().values('id', 'first_name' ,'last_name' ,'username','email','password')
        if user.exists():
            user_serializer = List_ClientSerializer(user, many = True)
            return Response(user_serializer.data, status= status.HTTP_200_OK)
        return Response({'message':"Clients don't exist"},status=status.HTTP_404_NOT_FOUND)
    
       
@api_view(['POST'])
def create_client_api_view(request):   
    # create
    if request.method == 'POST':
        user_serializer = Create_ClientSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'Successful registration'}, status= status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)