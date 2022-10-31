from django.shortcuts import render
from saude.forms import SaudeForms

# Create your views here.

def index (request):
    form= SaudeForms()
    contexto={'form': form}
    return render (request, 'index.html', contexto)


def revConsulta (request):
    if request.method == "POST":
        form= SaudeForms(request.POST)
        contexto={'form': form}
        return render (request, 'consulta.html', contexto)
