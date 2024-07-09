from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer
from .models import Utilisateur

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['username','first_name','last_name', 'email', 'date_of_birth','matricule', 'phone_number', 'profil_photo', 'password']  # Incluez les champs personnalisés ici
        extra_kwargs = {'password': {'write_only': True}}  # Assurez-vous que le champ du mot de passe est en écriture seule


class CustomUserSerializer(UserDetailsSerializer):
    phoneNumber = serializers.CharField(source='phone_number')
    date_nais = serializers.DateField(source='date_of_birth')
    photo = serializers.ImageField(source='profil_photo')
    matricule = serializers.CharField()

    class Meta(UserDetailsSerializer.Meta):
        model = Utilisateur
        fields = UserDetailsSerializer.Meta.fields + ('phoneNumber','date_nais','matricule','photo')


class CustomRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['username', 'first_name','last_name', 'matricule','email', 'date_of_birth', 'phone_number', 'profil_photo','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # créer un nouvel utilisateur avec les données validées
        user = Utilisateur.objects.create_user(**validated_data)
        return user