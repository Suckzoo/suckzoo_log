from django.db import models
from tags.models import Tag

class Cafe(models.Model):
    name = models.CharField(max_length=50)
    rating = models.FloatField(default=0, null=False)
    tags = models.ManyToManyField(Tag)
