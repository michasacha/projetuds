from rest_framework import serializers
from .models import Commande

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = ['id', 'user', 'menu', 'nombre_de_tickets', 'confirmed', 'created_at', 'updated_at']
        extra_kwargs = {
            'confirmed': {'read_only': True}
        }

    def create(self, validated_data):

        commande = Commande.objects.create(**validated_data, confirmed=True)
        return commande