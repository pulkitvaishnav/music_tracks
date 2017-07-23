from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from .models import Track, Genres
from .forms import TrackForm, GenresForm


def track_list(request):
    search_word = request.GET.get('search_box')
    if search_word:
        track_list = Track.objects.filter(Q(title__icontains=search_word) |
                                          Q(genre__genre__icontains=search_word))
    else:
        track_list = Track.objects.all()
    paginator = Paginator(track_list, 10)
    page = request.GET.get('page')
    try:
        tracks = paginator.page(page)
    except PageNotAnInteger:
        tracks = paginator.page(1)
    except EmptyPage:
        tracks = paginator.page(paginator.num_pages)
    context = {'track_list': tracks}
    return render(request, 'tracks/track_list.html', context)


def track_detail(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    return render(request, 'tracks/track_detail.html', {'track': track})


def add_track(request):
    if request.method == 'POST':
        form = TrackForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('Track:track_list')
    else:
        form = TrackForm
        
    return render(request, 'tracks/track_form.html', {'form': form})


def genre_list(request):
    genre_list = Genres.objects.all()
    paginator = Paginator(genre_list, 10)
    page = request.GET.get('page')
    try:
        genres = paginator.page(page)
    except PageNotAnInteger:
        genres = paginator.page(1)
    except EmptyPage:
        genres = paginator.page(paginator.num_pages)
    context = {'genre_list': genres}
    return render(request, 'genres/genre_list.html', context)


def genre_detail(request, genres_id):
    genres = get_object_or_404(Genres, pk=genres_id)
    return render(request, 'genres/genre_detail.html', {'genre': genres.genre})


def add_genres(request):
    if request.method == 'POST':
        form = GenresForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('Track:genre_list')
    else:
        form = GenresForm
        
    return render(request, 'genres/genre_form.html', {'form': form})
