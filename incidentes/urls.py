
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_incidentes, name='listar_incidentes'),  # Base URL to list incidents
    path('criar/', views.criar_incidente, name='criar_incidente'),
    path('listar/', views.listar_incidentes, name='listar_incidentes'),
]
