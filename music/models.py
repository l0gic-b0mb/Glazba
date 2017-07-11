from django.db import models
from django.core.urlresolvers import reverse


class Album(models.Model):
    artist = models.CharField(max_length=50)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def __str__(self):
        return "A " + self.genre + " album, " + self.album_title + " by " + self.artist

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={"pk": self.pk})
    #if new album created then where should it lead to ? This function does that, pk is hidden and sent as shown


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=100)
    file_type = models.CharField(max_length=10)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title + 'by ' + self.album.artist + ' in ' + self.album.album_title