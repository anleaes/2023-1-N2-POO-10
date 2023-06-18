from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'categorias'

router = routers.DefaultRouter()
router.register('categorias', views.CategoriaViewSet, basename='categorias')

urlpatterns = [
    path('', include(router.urls) )
]