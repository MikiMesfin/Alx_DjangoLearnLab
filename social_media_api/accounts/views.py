from django.shortcuts import render
from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from .serializers import UserSerializer

# Create your views here.

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        return Response({
            'token': token.key,
            'user': UserSerializer(user).data  
        })