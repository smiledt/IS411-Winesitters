from django.urls import path

from wine_recipes import views

app_name = 'wine_recipes'

urlpatterns = [
    # Index pattern
    path('', views.index, name='index'),

    # /wine_recipes pattern, this one will be the final
    path('wine_recipes/', views.recipes, name='wine_recipes'),
    path('new_recipe/', views.new_recipe, name='new_recipe')

]
