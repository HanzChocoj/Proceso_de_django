from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from apps.estudiantes.models import Student

class Publication(models.Model):
    title = models.CharField('Título', max_length=255)
    slug = models.SlugField('Slug', max_length=255, unique=True, blank=True)
    summary = models.CharField('Resumen', max_length=512, blank=True)
    content = models.TextField('Contenido')
    published = models.BooleanField('Publicado', default=False)
    published_at = models.DateTimeField('Fecha de publicación', auto_now_add=True)

    # FK al estudiante que publica (rol must be 'P')
    publisher = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='publications',
        limit_choices_to={'role': Student.ROLE_PUBLISHER},
        verbose_name='Publicado por'
    )
    # FK al estudiante que autoriza (rol must be 'A')
    autorizado_por = models.ForeignKey(
        Student,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='authorized_publications',
        limit_choices_to={'role': Student.ROLE_AUTHORIZER},
        verbose_name='Autorizado por'
    )

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-published_at']

    def clean(self):
        # Validación: publicador y autorizador no pueden ser la misma persona
        if self.publisher and self.autorizado_por and self.publisher == self.autorizado_por:
            raise ValidationError('El publicador y el autorizador deben ser personas distintas.')

    def save(self, *args, **kwargs):
        # Genera slug único automáticamente si no existe
        if not self.slug and self.title:
            base = slugify(self.title)[:200]
            slug = base
            i = 1
            while Publication.objects.filter(slug=slug).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        # Ejecuta validaciones
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
