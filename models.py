from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=200)
    developer = models.CharField(max_length=200, blank=True)
    site = models.URLField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    visible = models.BooleanField(default=False)
    buzz = models.IntegerField(default=0)
    rawbuzz = models.DecimalField(default=0, max_digits=14, decimal_places=2)
    plays = models.IntegerField(default=0)
    images = models.IntegerField(default=0, null=False, blank=False)
    opscomment = models.TextField(blank=True)
    platforms = models.ManyToManyField('Platform', related_name='games', null=True, blank=True)


class Platform(models.Model):
    name = models.CharField(max_length=200)

