from django.db import models

# Create your models here.


class Congestion(models.Model):
    line = models.PositiveSmallIntegerField()
    order = models.PositiveIntegerField()
    _from = models.PositiveIntegerField()
    _to = models.PositiveIntegerField()
    cong = models.FloatField()
    _in = models.PositiveIntegerField()
    _out = models.PositiveIntegerField()
    timestamp = models.DateTimeField()
