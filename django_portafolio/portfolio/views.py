from django.shortcuts import render, redirect
from .models import Proyecto
from .forms import ProyectoForm, RegistroForm
from django.contrib.auth.decorators import login_required

def index(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'portfolio/index.html', {'proyectos': proyectos})


@login_required
def crear_proyecto(request):
    if request.method == "POST":
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProyectoForm()

    return render(request, 'portfolio/crear_proyecto.html', {'form': form})

@login_required
def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("inicio")
    else:
        form = RegistroForm()

    