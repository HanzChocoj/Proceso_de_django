from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Publication, Comment
from .forms import PublicationForm, CommentForm


class publicacionesListView(ListView):
    model = Publication
    template_name = 'publicaciones_list.html'
    context_object_name = 'publicaciones'


class PublicationCreateView(CreateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'publicaciones_form.html'
    success_url = reverse_lazy('publicaciones:lista')


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments_form.html'
    success_url = reverse_lazy('publicaciones:publicaciones')
