from django.shortcuts import render, redirect
from wine_recipes.models import WineRecipe
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    """ Home Page for the wine_recipes app, may be temporary """
    return render(request, 'wine_recipes/index.html')


def recipes(request, message="", error=""):
    """ Displays all the recipes in a list """
    # Instantiate a dictionary of recipe objects
    recipes = WineRecipe.objects.order_by('name')
    recipe_dict = {'recipes': recipes}

    return render(request, 'wine_recipes/recipe_search.html', recipe_dict)


def view_recipe(request):
    """ Displays information about a specific recipe """
    if request.method == 'GET':
        # create a temp object to store the get info
        temp = request.GET['view_recipe']
        temp_recipe = WineRecipe.objects.get(name__startswith=temp)
        return render(request, 'wine_recipes/view_recipe.html', temp_recipe)


@login_required
def new_recipe(request):
    """ Add a new recipe """
    if request.method != 'POST':
        # form = RecipeForm()
        return redirect('wine_recipes:index')
    else:
        return redirect('wine_recipes:index')

        # form = RecipeForm(data=request.POST)
        # if form.is_valid():
        #     form.save()
        #     return recipes(request, message="Successfully created recipe:" + request.POST['recipe_name'])

    return redirect('wine_recipes:index')
