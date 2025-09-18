from django.urls import path
from .views import administradoresView, AdministradorCreateView

app_name = 'administradores'

urlpatterns = [
    path('', administradoresView.as_view(), name='administradores'),
    path('agregar/', AdministradorCreateView.as_view(), name='agregar'),
]
