from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import Entry, EntryImage
from .forms import EntryForm, EntryImageForm

def home(request):
    ImageFormSet = modelformset_factory(EntryImage, form=EntryImageForm, extra=3)

    if request.method == 'POST':
        form = EntryForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=EntryImage.objects.none())
        if form.is_valid() and formset.is_valid():
            entry = form.save()
            for image_form in formset.cleaned_data:
                if image_form:
                    EntryImage.objects.create(entry=entry, image=image_form['image'])
            return redirect('home')
    else:
        form = EntryForm()
        formset = ImageFormSet(queryset=EntryImage.objects.none())

    entries = Entry.objects.order_by('-created_at')
    return render(request, 'pitechblog/home.html', {'entries': entries, 'form': form, 'formset': formset})

