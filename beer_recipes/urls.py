from django.urls import path

from beer_recipes import views

app_name = 'beer_recipes'

urlpatterns = [

    # /beer_recipes pattern, this one will be the final contenttypes
    path('', views.recipes, name='beer_recipes'),
    path('new_recipe/', views.new_recipe, name='new_recipe')
]
