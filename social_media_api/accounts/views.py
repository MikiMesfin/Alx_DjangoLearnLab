from django.shortcuts import render
from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

# Create your views here.

 class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers']

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = CustomUser.objects.get(id=token.user_id)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })