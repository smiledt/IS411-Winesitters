from django import forms
from wine_recipes.models import WineRecipe

class RecipeForm(forms.ModelForm):
        """ This is the form for the creation of a new recipe """
        model = WineRecipe
        
