from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'autor'

router = routers.DefaultRouter()
router.register('autor', views.CategoryViewSet, basename='autor')

urlpatterns = [
    path('', include(router.urls) )
]