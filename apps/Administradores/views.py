from django.views.generic import ListView
from apps.estudiantes.models import Student

class administradoresView(ListView):
    model = Student
    template_name = 'administradores.html'
    context_object_name = 'administradores'

    def get_queryset(self):
        # Mostrar sólo estudiantes que son autorizadores
        return Student.objects.filter(role=Student.ROLE_AUTHORIZER).order_by('last_name', 'first_name')
