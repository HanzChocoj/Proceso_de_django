from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm

class estudiantesView(ListView):
    model = Student
    template_name = 'estudiantes_list.html'
    context_object_name = 'estudiantes'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'estudiantes_form.html'
    success_url = reverse_lazy('estudiantes:estudiantes')
