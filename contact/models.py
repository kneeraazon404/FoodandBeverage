from django.db import models
import datetime


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.CharField(max_length=2000, blank=True)
    contact_date = models.DateTimeField(default=datetime.datetime.now, blank=True)


def __str__(self):
    return self.name
