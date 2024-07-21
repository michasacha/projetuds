 
from rest_framework import generics
from .models import Repas, Menu
from .serializers import RepasSerializer, MenuSerializer

class RepasListCreateAPIView(generics.ListCreateAPIView):
    queryset = Repas.objects.all()
    serializer_class = RepasSerializer

class RepasRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Repas.objects.all()
    serializer_class = RepasSerializer

class MenuListCreateAPIView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
