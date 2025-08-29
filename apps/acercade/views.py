from django.shortcuts import render
from django.views.generic import TemplateView

class acercadeView(TemplateView):
    template_name = 'acercade.html'