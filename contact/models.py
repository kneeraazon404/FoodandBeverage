from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime


class Contact(models.Model):
    post_id = models.IntegerField(default=0)
    post = models.CharField(max_length=200, default=0)
    objects = models.Manager()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True, default="user_id")

    def __str__(self):
        return self.name
