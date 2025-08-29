from django.shortcuts import render
from django.views.generic import TemplateView

class administradoresView(TemplateView):
    template_name = 'administradores.html'