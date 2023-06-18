from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'biblioteca'

router = routers.DefaultRouter()
router.register('biblioteca', views.CategoryViewSet, basename='biblioteca')

urlpatterns = [
    path('', include(router.urls) )
]