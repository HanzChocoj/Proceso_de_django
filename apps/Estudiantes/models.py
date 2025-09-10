from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    ROLE_PUBLISHER = 'P'
    ROLE_AUTHORIZER = 'A'
    ROLE_CHOICES = [
        (ROLE_PUBLISHER, 'Publicante'),
        (ROLE_AUTHORIZER, 'Autorizador'),
    ]

    first_name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=100)
    email = models.EmailField('Email', unique=True)
    matricula = models.CharField('Matrícula', max_length=50, unique=True, null=True, blank=True)
    carrera = models.CharField('Carrera', max_length=120, blank=True)
    role = models.CharField('Rol', max_length=1, choices=ROLE_CHOICES, default=ROLE_PUBLISHER)
    created_at = models.DateTimeField('Creado', auto_now_add=True)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
