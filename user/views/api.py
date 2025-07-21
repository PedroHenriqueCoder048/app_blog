from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from user.models import User
from user.serializers import UserSerializer , UserLoginSerializer

import json

@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()

        serializer = UserSerializer(users,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','PUT','DELETE'])
def user_manager(request):
    
    if request.method =='GET':
        try:
            if request.GET['user_name']:
                user_name = request.GET['user_name']
                try:
                    user = User.objects.get(user_name=user_name)
                    seriealizer =UserSerializer(user)
                
                    return Response(seriealizer.data)
                except: 
                    return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    if request.method =='POST':
        
        new_user = request.data

        user_exist = User.objects.filter(
            Q(user_name=new_user['user_name']) | Q(email=new_user['email']) )

        if user_exist:
            return Response(status=status.HTTP_409_CONFLICT)

        seriealizer = UserSerializer(data=new_user)

        if seriealizer.is_valid():
            seriealizer.save()
            return Response({"response":"USR CREATED"}, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_BAD_REQUEST)
    
    if request.method == "PUT":

        user = request.data["user_name"]

        user_db = User.objects.get(
            Q(user_name=user) | Q(email=user))

        if not user_db:
            return Response(status=status.HTTP_409_CONFLICT)

        seriealizer = UserSerializer(user_db,data=request.data, partial = True)
        
        try:
            seriealizer.is_valid()
            seriealizer.save()
            return Response({"response":"USER UPDATED SUCESS"},status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == "DELETE":

        try:
            user_delete = User.objects.get(user_name=request.data["user_name"])
            user_delete.delete()
            return Response({"response":"USER DELETE SUCESS"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)