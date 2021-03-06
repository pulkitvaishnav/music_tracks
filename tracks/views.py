from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from .models import Track, Genres
from .forms import TrackForm, GenresForm


def track_list(request):
    """View to search on the basis of either music title or genre.
    If no filter is provided it return all tracks."""
    search_word = request.GET.get('search_box')
    if search_word:
        # Query to find all tracks which satisfy the above search term
        track_list = Track.objects.filter(Q(title__icontains=search_word) |
                                          Q(genre__genre__icontains=search_word))
    else:
        track_list = Track.objects.all()
    # Pagination tool to show only 10 tracks per page
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
    """View to return the individual track details"""
    track = get_object_or_404(Track, pk=track_id)
    return render(request, 'tracks/track_detail.html', {'track': track})


def add_track(request, pk=None):
    """View to add and edit any track"""
    try:
        instance = Track.objects.get(pk=pk)
    except Track.DoesNotExist:
        # if track is added for first time we add it to db.
        form = TrackForm(request.POST)
    else:
        # if app is already exist we edit that
        form = TrackForm(request.POST or None, instance=instance)
    # If requsted to edit
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('Track:track_detail', track_id=instance.pk)
    return render(request, "tracks/track_form.html", {'form': form})


def genre_list(request):
    """View to list all genre and paginated for 10 page per page."""
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
    """View to return an individual genre detail with all music tracks of it."""
    genres = get_object_or_404(Genres, pk=genres_id)
    return render(request, 'genres/genre_detail.html', {'genre': genres.genre,
                                                        'genre_track': genres.track.all()})


def add_genres(request):
    """View to add and edit any genre."""
    if request.method == 'POST':
        form = GenresForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('Track:genre_list')
    else:
        form = GenresForm
        
    return render(request, 'genres/genre_form.html', {'form': form})
