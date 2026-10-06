from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from flores.models import Planta
# Create your views here.

def home(request):
    plantas_data = Planta.objects.all()
    template = loader.get_template('index.html')
    context = {
        'data':plantas_data
    }
    return HttpResponse(template.render(context, request))

def planta(request, id):
    plantas_data = Planta.objects.get(id=id)
    template = loader.get_template('detalhe.html')
    context = {
        'data':plantas_data
    }
    return HttpResponse(template.render(context, request))
    