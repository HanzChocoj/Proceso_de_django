from django.urls import path
from .views import publicacionesListView, PublicationCreateView, CommentCreateView

app_name = 'publicaciones'

urlpatterns = [
    path('', publicacionesListView.as_view(), name='lista'),  # lista de publicaciones
    path('agregar/', PublicationCreateView.as_view(), name='agregar'),  # crear publicación
    path('comentario/agregar/', CommentCreateView.as_view(), name='agregar_comentario'),  # crear comentario
]

