from .models import Categoria
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']