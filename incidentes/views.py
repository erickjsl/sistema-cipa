
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import IncidenteForm
from .models import Incidentes
from django.http import HttpResponse

@login_required
def index(request):
    return HttpResponse("Hello, this is the incident report index.")

@login_required
def criar_incidente(request):
    if request.method == 'POST':
        form = IncidenteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_incidentes')
    else:
        form = IncidenteForm()
    return render(request, 'incidentes/criar_incidente.html', {'form': form})

@login_required
def listar_incidentes(request):
    incidentes = Incidentes.objects.all()
    return render(request, 'incidentes/listar_incidentes.html', {'incidentes': incidentes})
