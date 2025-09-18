from django.urls import path
from .views import estudiantesView, StudentCreateView

app_name = 'estudiantes'

urlpatterns = [
    path('', estudiantesView.as_view(), name='estudiantes'),
    path('agregar/', StudentCreateView.as_view(), name='estudiantes_agregar'),
]
