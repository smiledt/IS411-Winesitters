from django import forms
from beer_recipes.models import BeerRecipe, Hop, Fermentable, Yeast, Water, Misc


class RecipeForm(forms.ModelForm):
    # TODO: Add validation here
    class Meta:
        model = BeerRecipe
        fields = ['name', 'description', 'brewer',
                  'batch_size', 'boil_size', 'boil_time', 'type']


class HopForm(forms.ModelForm):
    # TODO: Add validation here
    class Meta:
        model = Hop
        exclude = ['version', 'date_submitted', 'user']


class FermentableForm(forms.ModelForm):
    # TODO: Add validation here
    class Meta:
        model = Fermentable
        exclude = ['version', 'date_submitted', 'user']


class YeastForm(forms.ModelForm):
    # TODO: Add validation here
    class Meta:
        model = Yeast
        exclude = ['version', 'date_submitted', 'user']


class MiscForm(forms.ModelForm):
    # TODO: Add validation here
    class Meta:
        model = Misc
        exclude = ['version', 'date_submitted', 'user']


class WaterForm(forms.ModelForm):
    # TODO: Add validation here
    class Meta:
        model = Water
        exclude = ['version', 'date_submitted', 'user']
