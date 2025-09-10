from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Publication

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'autorizado_por', 'published', 'published_at')
    list_filter = ('published', 'published_at')
    search_fields = ('title', 'summary', 'content')
    prepopulated_fields = {'slug': ('title',)}
