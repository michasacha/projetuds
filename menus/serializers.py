from rest_framework import serializers
from .models import Repas, Menu

class RepasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repas
        fields = ['id', 'name', 'photo']
        

class MenuSerializer(serializers.ModelSerializer):
    repas = RepasSerializer() 

    class Meta:
        model = Menu
        fields = ['id', 'date', 'repas']

    def create(self, validated_data):
            repas_data = validated_data.pop('repas')
            repas =  Repas.objects.create(** repas_data)
            menu = Menu.objects.create( repas= repas, **validated_data)
            return menu