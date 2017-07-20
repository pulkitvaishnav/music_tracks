from django.db import models


class Genres(models.Model):
    """Model to store all genres"""
    genre = models.CharField(max_length=30, unique=True, blank=False)


class Track(models.Model):
    """Model to store track of music (Took assumtion that title won't
    be bigger then 200 chars)"""
    title = models.CharField(max_length=200, unique=True, blank=False)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    rating = models.IntegerField()

