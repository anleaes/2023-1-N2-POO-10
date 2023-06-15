from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'editoras'

router = routers.DefaultRouter()
router.register('editoras', views.EditoraViewSet, basename='editoras')

urlpatterns = [
    path('', include(router.urls) )
]
