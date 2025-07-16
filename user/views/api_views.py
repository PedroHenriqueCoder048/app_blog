from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from user.models import User
from user.serializers import UserSerializer

import json

@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()

        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user(request,user_name):

    try:
        User.objects.get(user_name=user_name)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        seriealizer = UserSerializer(user_name)
        return Response(seriealizer.data)