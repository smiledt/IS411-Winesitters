from django import forms
from beer_recipes.models import BeerRecipe


class RecipeForm(forms.ModelForm):
    # TODO: Add validation here
    class Meta:
        model = BeerRecipe
        fields = ['name', 'description', 'brewer',
                  'batch_size', 'boil_size', 'boil_time', 'type']
