from django.db import models
from datetime import datetime


class InfoBox(models.Model):
    Id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=120)
    City = models.CharField(max_length=40)
    Time = models.DateTimeField(default=datetime.now())
    Rolik = models.URLField()
    ClickNumbes = models.IntegerField()
