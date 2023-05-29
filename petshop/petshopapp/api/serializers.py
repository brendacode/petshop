from rest_framework import serializers
from petshopapp import models


class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cadastro
        fields = '__all__'
        
class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Produtos
        fields = '__all__'

class ServicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Servicos
        fields = '__all__'