from django.db import models


# Create your models here.
class Articles(models.Model):
    heading = models.CharField(max_length=500)
    body = models.CharField(max_length=2000)
    category = models.CharField(max_length=100)
    content_type = models.CharField(max_length=100)
    source_link = models.CharField(max_length=1000)
    image_link = models.CharField(max_length=1000)
    tags = models.CharField(max_length=100)
    published_date = models.DateField()
    published_time = models.TimeField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.heading
