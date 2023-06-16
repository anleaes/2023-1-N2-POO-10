from django.shortcuts import render
from .models import Emprestimo
from rest_framework import viewsets
from .serializer import EmprestimoSerializer
# Create your views here.
class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
