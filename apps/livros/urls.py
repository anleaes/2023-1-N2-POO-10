from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'livros'

router = routers.DefaultRouter()
router.register('livros', views.CategoryViewSet, basename='livros')

urlpatterns = [
    path('', include(router.urls) )
]