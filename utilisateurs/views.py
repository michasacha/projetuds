from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import CustomRegisterSerializer

class CustomUserCreateView(generics.CreateAPIView):
    # utiliser le serializer pour créer un nouvel utilisateur
    serializer_class = CustomRegisterSerializer