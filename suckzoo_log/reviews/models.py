from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from cafes.models import Cafe
from users.models import User

class Review(models.Model):
    content = models.TextField()
    rating = models.FloatField(null=False, \
	    validators = [MinValueValidator(0), MaxValueValidator(5)])
    cafe = models.ForeignKey(Cafe)
    author = models.ForeignKey(User)
    # @TODO: images = 
