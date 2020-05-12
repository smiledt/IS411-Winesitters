from django.urls import path

from beer_recipes import views


app_name = 'beer_recipes'

urlpatterns = [

    # /beer_recipes pattern, this one will be the final
    path('', views.index, name='index'),
    path('my_ingredients/', views.my_ingredients, name='my_ingredients'),  # Lists a users ingredients
    path('my_recipes/', views.my_recipes, name='my_recipes'),  # Lists a users recipes
    path('recipes/', views.recipes, name='recipes'),  # Lists all recipes
    path('ingredients/', views.ingredients, name='ingredients'),  # Lists all ingredients

    # All create url paths -------------------
    path('new_recipe/', views.new_recipe, name='new_recipe'),
    path('new_hop', views.new_hop, name='new_hop'),
    path('new_fermentable', views.new_fermentable, name='new_fermentable'),
    path('new_misc', views.new_misc, name='new_misc'),
    path('new_water', views.new_water, name='new_water'),
    path('new_yeast', views.new_yeast, name='new_yeast'),

    # All view url paths ----------------------
    path('view_recipe/<int:pk>', views.RecipeDetails.as_view(), name='RecipeDetails'),
    path('view_hop/<int:pk>', views.HopDetails.as_view(), name='HopDetails'),
    path('view_fermentable/<int:pk>', views.FermentableDetails.as_view(), name='FermentableDetails'),
    path('view_misc/<int:pk>', views.MiscDetails.as_view(), name='MiscDetails'),
    path('view_water/<int:pk>', views.WaterDetails.as_view(), name='WaterDetails'),
    path('view_yeast/<int:pk>', views.YeastDetails.as_view(), name='YeastDetails'),

    # All edit url paths -----------------------
    path('edit_recipe/', views.edit_recipe, name='edit_recipe'),
    path('update_hop/<int:pk>', views.HopUpdate.as_view(), name='HopUpdate'),
    path('edit_fermentable/<int:pk>', views.FermentableUpdate.as_view(), name='FermentableUpdate'),
    path('edit_misc/<int:pk>', views.MiscUpdate.as_view(), name='MiscUpdate'),
    path('edit_water/<int:pk>', views.WaterUpdate.as_view(), name='WaterUpdate'),
    path('edit_yeast/<int:pk>', views.YeastUpdate.as_view(), name='YeastUpdate'),

    # All delete url paths ----------------------------------------------------
    path('delete_hop/<int:pk>', views.HopDelete.as_view(), name='HopDelete'),
    path('delete_fermentable/<int:pk>', views.FermentableDelete.as_view(), name='FermentableDelete'),
    path('delete_misc/<int:pk>', views.MiscDelete.as_view(), name='MiscDelete'),
    path('delete_water/<int:pk>', views.WaterDelete.as_view(), name='WaterDelete'),
    path('delete_yeast/<int:pk>', views.YeastDelete.as_view(), name='YeastDelete'),

]
