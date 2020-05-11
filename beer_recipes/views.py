from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from beer_recipes.models import BeerRecipe
from beer_recipes.forms import RecipeForm, HopForm, FermentableForm, YeastForm, WatersForm, MiscForm

# Create your views here.


def index(request):
    """ Home Page for the beer_recipes app, may be temporary """
    return render(request, 'beer_recipes/index.html')


def recipes(request, error="", message=""):
    """ Displays all the recipes in a list """
    # Instantiate a dictionary of recipe objects
    recipes = BeerRecipe.objects.order_by('name')
    recipe_dict = {'recipes': recipes, 'error': error, 'message': message}

    return render(request, 'beer_recipes/recipe_search.html', recipe_dict)


def view_recipe(request, error="", message=""):
    """ Displays information about a specific recipe """
    if request.method == 'GET':
        # create a temp object to store the get info
        temp = request.GET['view_recipe']
        temp_recipe = BeerRecipe.objects.get(name=temp)
        return render(request, 'beer_recipes/view_recipe.html', temp_recipe)


def search_recipe(request):
    """ Searches for a specific recipe """
    if request.method == 'GET':
        if 'recipe_search' not in request.GET:  # User clicked search with an empty bar
            error = 'Please enter a recipe.'
            recipes = BeerRecipe.objects.order_by('name')
            return recipes(request, error=error)
        else:
            recipes = BeerRecipe.objects.filter(
                name__contains=request.GET['recipe_search'].lower())
            if recipes:
                print("IT WORKED")  # TODO: Debug code, delete later
                message = 'Search for ' + request.GET['recipe_search'] + ":"
                return recipes(request, message=message)
            else:
                error = 'Sorry, no recipes matched your search. Try again, or add a recipe below!'
                return recipes(request, error=error)


@login_required
def new_recipe(request):
    """ Add a new recipe """
    if request.method != 'POST':
        form = RecipeForm()
    else:
        form = RecipeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return recipes(request, message="Successfully created recipe: " + request.POST['recipe_name'])

    context = {'form': form}
    # TODO: Start here tomorrow, create templates
    return render('beer_recipes/new_recipe.html', context)


@login_required
def new_hop(request):
    """ Creates a new hop """
    if request.method != 'POST':
        form = HopForm()
    else:
        form = HopForm(data=request.POST)
        if form.is_valid():
            form.save()
            return recipes(request, message="Successfully created hop: " + request.POST['recipe_name'])

    context = {'form': form}
    # TODO: Start here tomorrow, create templates
    return render('beer_recipes/new_hop.html', context)


@login_required
def new_fermentable(request):
    """ Creates a new fermentable """
    if request.method != 'POST':
        form = FermentableForm()
    else:
        form = FermentableForm(data=request.POST)
        if form.is_valid():
            form.save()
            return recipes(request, message="Successfully created fermentable: " + request.POST['recipe_name'])

    context = {'form': form}
    # TODO: Start here tomorrow, create templates
    return render('beer_recipes/new_fermentable.html', context)


@login_required
def new_yeast(request):
    """ Creates a new yeast """
    if request.method != 'POST':
        form = YeastForm()
    else:
        form = YeastForm(data=request.POST)
        if form.is_valid():
            form.save()
            return recipes(request, message="Successfully created yeast: " + request.POST['recipe_name'])

    context = {'form': form}
    # TODO: Start here tomorrow, create templates
    return render('beer_recipes/new_yeast.html', context)


@login_required
def new_misc(request):
    """ Creates a new miscellaneous ingredient """
    if request.method != 'POST':
        form = MiscForm()
    else:
        form = MiscForm(data=request.POST)
        if form.is_valid():
            form.save()
            return recipes(request, message="Successfully created ingredient: " + request.POST['recipe_name'])

    context = {'form': form}
    # TODO: Start here tomorrow, create templates
    return render('beer_recipes/new_misc.html', context)


@login_required
def new_water(request):
    """ Creates a new water profile """
    if request.method != 'POST':
        form = WatersForm()
    else:
        form = WatersForm(data=request.POST)
        if form.is_valid():
            form.save()
            return recipes(request, message="Successfully created water profile: " + request.POST['recipe_name'])

    context = {'form': form}
    # TODO: Start here tomorrow, create templates
    return render('beer_recipes/new_water.html', context)
