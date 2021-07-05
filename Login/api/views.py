from django.http import request
from Login import api
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from Login.views import Default
from django.contrib.auth import authenticate, login, logout
from Login.api.serializers import User, UserSerializer, UserNameSerializer, CreateUserSerializer

@api_view(['POST'])
def userName(request):
    if request.method=="POST":
        ser=UserNameSerializer(data=request.data)

        if ser.is_valid():
            username = ser.data['username']
            valid = True
            if User.objects.filter(username=username).exists():
                valid=False
            data ={'valid':valid}
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signUp(request):
    if request.method=="POST":
        ser = CreateUserSerializer(data=request.data)
        if ser.is_valid():
            user_obj = User(username = ser.data['username'], email=ser.data['email'])
            user_obj.set_password(ser.data['password'])
            user_obj.save()
            data={'valid':True}
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logIn(request):
    if not("username" in request.data and "password" in request.data):
        return Response({'err':"field is required"},status=status.HTTP_400_BAD_REQUEST)
    ser=UserSerializer(data=request.data)
    if ser.is_valid():
        username = ser.data['username']
        password=ser.data['password']
    else:
        username = ser.data['username']
        password=ser.data['password']
    if not(User.objects.filter(username=username).exists()):
        msg = 'User Name is not exists'
        usr, pwd='', ''
    elif not(User.objects.filter(username=username, password=password).exists()):
        msg='Password is incorrect'
        usr, pwd=username, ''
    else:
        msg, usr, pwd='','',''
    user = authenticate(request, username=username, password=password)
    valid=False
    if user is not None:
        valid=True
    data ={'valid':valid, 'msg':msg, 'username':usr, 'pwd':pwd}
    return Response(data,status=status.HTTP_200_OK)
