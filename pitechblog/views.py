from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Entry
from .forms import EntryForm

#view
def home(request):
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = EntryForm()

    entries = Entry.objects.order_by('-created_at')
    return render(request, 'pitechblog/home.html', {'entries': entries, 'form': form})
    
