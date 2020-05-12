from django.db import models
from datetime import date
from django import forms

# Create your models here.


class WineRecipe(models.Model):
    """ This is a recipe that a user creates """

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True)
    date_submitted = models.DateField(auto_now_add=True)
    version = models.PositiveIntegerField(default=1)
