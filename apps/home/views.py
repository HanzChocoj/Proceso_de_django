from django.shortcuts import render
from django.views.generic import TemplateView

class homeview(TemplateView):
    template_name = 'home.html'

class listadoview(TemplateView):
    template_name = 'listado.html'    
# Create your views here.

