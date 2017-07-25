from django import forms
from .models import Track, Genres


class GenresForm(forms.ModelForm):
    """Form for genre"""

    class Meta:
        model = Genres
        fields = ['genre']


class TrackForm(forms.ModelForm):
    """Form to add a track"""
    
    class Meta:
        model = Track
        fields = ['title', 'genre', 'rating']
    # Customized the rating field so that one can add only 5,4 .. 1 only
    RATING_CHOICES = ((5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1'))
    rating = forms.TypedChoiceField(choices=RATING_CHOICES,
                                    widget=forms.RadioSelect, coerce=int)
