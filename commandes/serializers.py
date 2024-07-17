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
        code_pin = validated_data.pop('code_pin')
        confirmed_code_pin = self.context.get('confirmed_code_pin')

        if code_pin != confirmed_code_pin:
            raise serializers.ValidationError("Pin codes do not match.")

        commande = Commande.objects.create(**validated_data, confirmed=True)
        return commande
