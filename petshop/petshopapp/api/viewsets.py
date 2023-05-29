from rest_framework import viewsets
from petshopapp.api import serializers
from petshopapp import models
from django.shortcuts import render, redirect


class CadastroViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CadastroSerializer
    queryset = models.Cadastro.objects.all()

class ProdutosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProdutosSerializer
    queryset = models.Produtos.objects.all()
    
class ServicosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ServicosSerializer
    queryset = models.Servicos.objects.all()
