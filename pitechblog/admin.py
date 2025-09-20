from django.contrib import admin
from .models import Entry, EntryImage

class EntryImageInline(admin.TabularInline):
    model = EntryImage
    extra = 3  # ile pustych pól obrazów pokazać

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    inlines = [EntryImageInline]  # dodajemy inline
