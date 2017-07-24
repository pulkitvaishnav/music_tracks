from django import forms
from .models import Track, Genres


class GenresForm(forms.ModelForm):

    class Meta:
        model = Genres
        fields = ['genre']


class TrackForm(forms.ModelForm):
    
    class Meta:
        model = Track
        fields = ['title', 'genre', 'rating']

    RATING_CHOICES = ((5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1'))
    rating = forms.TypedChoiceField(choices=RATING_CHOICES,
    								widget=forms.RadioSelect, coerce=int)
