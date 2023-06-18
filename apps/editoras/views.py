#from django.shortcuts import render
from .models import Editora
from rest_framework import viewsets
from .serializer import EditoraSerializer
# Create your views here.
class EditoraViewSet(viewsets.ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
