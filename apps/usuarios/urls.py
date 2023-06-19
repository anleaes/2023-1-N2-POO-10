from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'usuarios'

router = routers.DefaultRouter()
router.register('usuarios', views.UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls) )
]