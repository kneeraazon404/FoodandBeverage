from django.db import models
from datetime import datetime
import re


class Post(models.Model):
    title = models.CharField(max_length=200)
    videoUrl = "https://www.youtube.com/watch?v=X3iFhLdWjqc"
    embedUrl = re.sub(
        r"(?ism).*?=(.*?)$", r"https://www.youtube.com/embed/\1", videoUrl
    )
    description = models.TextField(blank=True)
    post_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
