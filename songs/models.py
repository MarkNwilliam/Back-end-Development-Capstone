from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200, blank=True)
    year = models.IntegerField(default=0)
    lyrics = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"
