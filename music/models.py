from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255, null=False)
    artist = models.CharField(max_length=255, null=False)
    album = models.CharField(max_length=255, blank=True)
    song_file = models.FileField(upload_to='', null=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)
