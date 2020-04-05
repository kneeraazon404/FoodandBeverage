from django.db import models
from datetime import datetime
from embed_video.fields import EmbedVideoField


class Post(models.Model):
    title = models.CharField(max_length=200)
    video = EmbedVideoField(max_length=140, default="SOME STRING")
    description = models.TextField(blank=True)
    post_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
