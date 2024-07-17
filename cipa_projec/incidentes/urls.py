from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_incidente, name='criar_incidente'),
    path('', views.listar_incidentes, name='listar_incidentes'),
]
