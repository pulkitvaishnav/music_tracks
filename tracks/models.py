from django.db import models


class Genres(models.Model):
    """Model to store all genres"""
    genre = models.CharField(max_length=30, unique=True, blank=False)

    def __str__(self):
        return self.genre


class Track(models.Model):
    """Model to store track of music (Took assumtion that title won't
    be bigger then 200 chars)"""
    title = models.CharField(max_length=200, unique=True, blank=False)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE,
                              related_name='track')
    rating = models.IntegerField()

    def __str__(self):
        return self.title

