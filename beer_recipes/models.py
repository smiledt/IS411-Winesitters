from django.db import models
from datetime import date
from django import forms

# Create your models here.


class BeerRecipe(models.Model):
    """ This is a recipe that a user creates """

    name = models.CharField(max_length=200)
    description = models.TextField()
    date_submitted = models.DateField(auto_now_add=True)
