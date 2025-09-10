from django.views.generic import ListView
from .models import Student

class estudiantesView(ListView):
    model = Student
    template_name = 'estudiantes.html'
    context_object_name = 'estudiantes'

    def get_queryset(self):
        # Mostrar sólo estudiantes que son publicantes
        return Student.objects.filter(role=Student.ROLE_PUBLISHER).order_by('last_name', 'first_name')
