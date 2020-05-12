from django.contrib import admin
from beer_recipes.models import BeerRecipe, Hop, Fermentable, Yeast, Water, Misc

# Register your models here.
admin.site.register(BeerRecipe)
admin.site.register(Hop)
admin.site.register(Fermentable)
admin.site.register(Yeast)
admin.site.register(Water)
admin.site.register(Misc)
