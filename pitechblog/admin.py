from django.contrib import admin
from .models import Entry

# Register models


from django.contrib import admin
from .models import Entry

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # kolumny w panelu listy
    list_filter = ('created_at',)          # filtr po dacie
    search_fields = ('title', 'content')   # wyszukiwanie po tytule i treści
