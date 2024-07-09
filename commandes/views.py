from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Commande
from .serializers import CommandeSerializer

class CommandeCreateView(generics.CreateAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['confirmed_code_pin'] = self.request.data.get('confirmed_code_pin')
        return context

