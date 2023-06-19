from django.shortcuts import render
from .models import Livro
from rest_framework import viewsets
from .serializer import LivroSerializer

# Create your views here.

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer