
from django.shortcuts import render, redirect
from .forms import IncidenteForm
from .models import Incidentes  # Corrigido aqui
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the incident report index.")

def criar_incidente(request):
    if request.method == 'POST':
        form = IncidenteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_incidentes')
    else:
        form = IncidenteForm()
    return render(request, 'incidentes/criar_incidente.html', {'form': form})

def listar_incidentes(request):
    incidentes = Incidentes.objects.all()  # Corrigido aqui
    return render(request, 'incidentes/listar_incidentes.html', {'incidentes': incidentes})
