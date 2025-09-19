from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Administrador
from .forms import AdministradorForm

# Lista de administradores
class administradoresView(ListView):
    model = Administrador
    template_name = 'administradores_list.html'  
    context_object_name = 'administradores'

# Crear administrador
class AdministradorCreateView(CreateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = 'administradores_form.html'  
    success_url = reverse_lazy('administradores:administradores')  
