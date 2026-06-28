from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
