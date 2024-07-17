# etudiants/urls.py
from django.urls import path 
from .views import EtudiantListCreate, EtudiantRetrieveUpdateDestroy

urlpatterns = [
    path('etudiants/', EtudiantListCreate.as_view(), name='etudiant-list-create'),
    path('etudiants/<str:matricule>/', EtudiantRetrieveUpdateDestroy.as_view(), name='etudiant-detail'),
]
 