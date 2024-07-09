from rest_framework import serializers

class DepotSerializer(serializers.Serializer):
    montant = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_montant(self, value):
        if value <= 100:
            raise serializers.ValidationError("Le montant du dépôt doit être supérieur à cent.")
        return value

class RetraitSerializer(serializers.Serializer):
    montant = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_montant(self, value):
        if value <= 100:
            raise serializers.ValidationError("Le montant du retrait doit être supérieur à cent.")
        return value
