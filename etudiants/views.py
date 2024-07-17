from django.shortcuts import render
from rest_framework import generics
from .models import Etudiant
from .serializers import EtudiantSerializer

class EtudiantListCreate(generics.ListCreateAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer

class EtudiantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    lookup_field = 'matricule'

