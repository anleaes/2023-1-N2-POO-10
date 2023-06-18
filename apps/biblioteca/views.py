from django.shortcuts import render
from .models import Biblioteca
from rest_framework import viewsets
from .serializer import BibliotecaSerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer