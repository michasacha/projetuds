from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
# Create your views here.
from rest_framework import generics
from .serializers import CustomRegisterSerializer

class CustomUserCreateView(generics.CreateAPIView):
    
    permission_classes = (AllowAny,)
    # utiliser le serializer pour créer un nouvel utilisateur
    serializer_class = CustomRegisterSerializer