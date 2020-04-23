from django.db import models
from datetime import datetime

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="photos/%y/%m/%d/")
    position = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100)
    description = models.TextField(max_length=1000, default="I Can do anything")
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
