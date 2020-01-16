from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to="photos/%y/%m/%d/")
    description = models.TextField(blank=True)
    url = models.URLField(max_length=500, blank=True)
    post_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

