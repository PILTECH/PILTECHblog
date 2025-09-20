from django import forms
from .models import Entry, EntryImage

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content']

class EntryImageForm(forms.ModelForm):
    class Meta:
        model = EntryImage
        fields = ['image']
