# etudiants/serializers.py
from rest_framework import serializers
from .models import Etudiant

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = ['matricule', 'nom', 'prenom']
