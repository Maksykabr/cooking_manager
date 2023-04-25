from django.contrib.auth.models import User
from django.db import models


class Day_of_week(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    description = models.TextField()
    ingredients = models.TextField()
    serving = models.CharField(max_length=10)
    time = models.CharField(max_length=5)
    Day_of_week = models.ForeignKey(Day_of_week, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    uploaded = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

