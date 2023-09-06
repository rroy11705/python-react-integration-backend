from django.db import models


class StreamPlatform(models.Model):
    name = models.CharField(max_length=64)
    about = models.TextField(max_length=512)
    website = models.URLField(max_length=128)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=256)
    storyline = models.TextField(max_length=2048)
    platforms = models.ManyToManyField(StreamPlatform, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title