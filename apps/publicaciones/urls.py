from django.urls import path
from .views import publicacionesListView, PublicationCreateView, CommentCreateView

app_name = 'publicaciones'

urlpatterns = [
    path('', publicacionesListView.as_view(), name='lista'),  
    path('agregar/', PublicationCreateView.as_view(), name='agregar'),  
    path('comentario/agregar/', CommentCreateView.as_view(), name='agregar_comentario'),  
]

