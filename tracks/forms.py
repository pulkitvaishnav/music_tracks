from django.forms import ModelForm
from .models import Track, Genres


class GenresForm(ModelForm):
    class Meta:
        model = Genres
        fields = ['genre']


class TrackForm(ModelForm):
    class Meta:
        model = Track
        fields = ['title', 'genre', 'rating']
