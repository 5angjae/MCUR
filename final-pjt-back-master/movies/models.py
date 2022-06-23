from django.core import validators
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields import related


class Movie(models.Model):
    tmdb_id = models.IntegerField(default=0)
    type = models.CharField(max_length=10, default="movie")
    heros = models.TextField(default='')
    cookie_movie_id = models.IntegerField(null=True)

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_reviews")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_reviews")
    title = models.CharField(max_length=50)
    rank = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)])
    content = models.TextField()

