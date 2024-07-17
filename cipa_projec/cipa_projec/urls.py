
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('incidentes/', include('incidentes.urls')),
    path('accounts/', include('accounts.urls')),
    path('', lambda request: redirect('home', permanent=True)),  # Redirecionar para a página principal
]
