from django.db import models


# Create your models here.
class Feeds(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=1000)
    published = models.DateTimeField()
    website = models.CharField(max_length=100)
    category = models.CharField(max_length=100)