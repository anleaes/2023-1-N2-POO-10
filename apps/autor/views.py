#from django.shortcuts import render
from .models import Autor
from rest_framework import viewsets
from .serializer import AutorSerializer
# Create your views here.
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer