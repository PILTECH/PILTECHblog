from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Napisz'})
        }
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and image.size > 2*1024*1024:  # 2MB
            raise forms.ValidationError("Obrazek nie może być większy niż 2MB")
        return image