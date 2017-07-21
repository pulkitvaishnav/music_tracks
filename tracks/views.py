from django import forms
from django.shortcuts import render
from .models import Track
from .forms import TrackForm, GenresForm

def add_track(request):
    if request.method == 'POST':
        form = TrackForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('tracks-add')
    else:
        form = TrackForm
        
    return render(request, 'tracks/track_form.html', {'form': form})


def add_genres(request):
    if request.method == 'POST':
        form = GenresForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('tracks-add')
    else:
        form = GenresForm
        
    return render(request, 'genres/genre_form.html', {'form': form})