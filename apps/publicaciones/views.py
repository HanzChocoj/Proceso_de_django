from django.views.generic import ListView
from .models import Publication

class publicacionesListView(ListView):
    model = Publication
    template_name = 'publicaciones.html'
    context_object_name = 'publicaciones'
    queryset = Publication.objects.select_related('publisher', 'autorizado_por').order_by('-published_at')
