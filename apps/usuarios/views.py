#from django.shortcuts import render
from .models import Usuario
from rest_framework import viewsets
from .serializer import UsuarioSerializer

# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    fields = "__all__"