from django.urls import path
from .views import publicacionesListView

app_name = 'publicaciones'
urlpatterns = [
    path('', publicacionesListView.as_view(), name='lista'),
]
