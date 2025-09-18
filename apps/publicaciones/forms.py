from django import forms
from .models import Publication, Comment

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'summary', 'content', 'published', 'publisher', 'autorizado_por']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['publication', 'student', 'content']
