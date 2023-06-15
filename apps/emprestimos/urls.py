from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'emprestimos'

router = routers.DefaultRouter()
router.register('emprestimos', views.EmprestimoViewSet, basename='emprestimos')

urlpatterns = [
    path('', include(router.urls) )
]