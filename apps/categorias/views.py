#from django.shortcuts import render
from .models import Categoria
from rest_framework import viewsets
from .serializer import CategoriaSerializer

# Create your views here.

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer