from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from beer_recipes.models import BeerRecipe, Hop, Fermentable, Yeast, Water, Misc
from beer_recipes.forms import RecipeForm, HopForm, FermentableForm, YeastForm, WaterForm, MiscForm

# Create your views here.


def index(request):
    """ Home Page for the beer_recipes app, may be temporary """
    return recipes(request)


#  List views here ------------------------------------------------------------
def recipes(request, error="", message=""):
    """ Displays all the recipes in a list """
    # Instantiate a dictionary of recipe objects
    recipes = BeerRecipe.objects.order_by('name')
    recipe_dict = {'recipes': recipes, 'error': error, 'message': message}

    return render(request, 'beer_recipes/recipe_list.html', recipe_dict)


# Eventually only admins should call this, don't know Jimmy's admin function
def ingredients(request, error="", message=""):
    """ Displays all the ingredients in a list """
    # Instantiate a dictionary of ingredients objects
    ingredients_dict = {'error': error, 'message': message}
    hops = Hop.objects.order_by('name')
    fermentables = Fermentable.objects.order_by('name')
    miscs = Misc.objects.order_by('name')
    waters = Water.objects.order_by('name')
    yeasts = Yeast.objects.order_by('name')
    ingredients_dict.update({'hops': hops, 'fermentables': fermentables,
                             'miscs': miscs, 'waters': waters, 'yeasts': yeasts})
    return render(request, 'beer_recipes/list_ingredients.html', ingredients_dict)


@login_required
def my_ingredients(request, error="", message=""):
    """ Displays all the users ingredients """
    ingredients_dict = {'error': error, 'message': message}

    current_user = request.user
    hops = Hop.objects.filter(user=current_user.username)
    fermentables = Fermentable.objects.filter(user=current_user.username)
    miscs = Misc.objects.filter(user=current_user.username)
    waters = Water.objects.filter(user=current_user.username)
    yeasts = Yeast.objects.filter(user=current_user.username)
    ingredients_dict.update({'hops': hops, 'fermentables': fermentables,
                             'miscs': miscs, 'waters': waters, 'yeasts': yeasts})
    return render(request, 'beer_recipes/list_ingredients.html', ingredients_dict)


@login_required
def my_recipes(request, error="", message=""):
    """ Displays all the users ingredients """
    recipes_dict = {'error': error, 'message': message}

    if request.method == 'GET':
        current_user = request.user

    return redirect('beer_recipes:index')


#  New views here -------------------------------------------------------------
@login_required
def new_recipe(request):
    """ Add a new recipe """
    if request.method != 'POST':
        form = RecipeForm()
    else:
        form = RecipeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return recipes(request, message="Successfully created recipe: " + request.POST['name'])

    context = {'form': form}
    # TODO: Start here tomorrow, create templates
    return render(request, 'beer_recipes/new_recipe.html', context)


@login_required
def new_hop(request):
    """ Creates a new hop """
    if request.method != 'POST':
        form = HopForm()
    else:
        form = HopForm(data=request.POST)
        if form.is_valid():
            new_hop = form.save(commit=False)
            new_hop.user = request.user.username
            new_hop.save()
            return my_ingredients(request, message="Successfully created hop: " + request.POST['name'])

    context = {'form': form}
    # TODO: Start here tomorrow, create templates
    return render(request, 'beer_recipes/new_hop.html', context)


@login_required
def new_fermentable(request):
    """ Creates a new fermentable """
    if request.method != 'POST':
        form = FermentableForm()
    else:
        form = FermentableForm(data=request.POST)
        if form.is_valid():
            new_ferm = form.save(commit=False)
            new_ferm.user = request.user.username
            new_ferm.save()
            return my_ingredients(request, message="Successfully created fermentable: " + request.POST['name'])

    context = {'form': form}
    # TODO: Start here tomorrow, create templates
    return render(request, 'beer_recipes/new_fermentable.html', context)


@login_required
def new_yeast(request):
    """ Creates a new yeast """
    if request.method != 'POST':
        form = YeastForm()
    else:
        form = YeastForm(data=request.POST)
        if form.is_valid():
            new_yeast = form.save(commit=False)
            new_yeast.user = request.user.username
            new_yeast.save()
            return my_ingredients(request, message="Successfully created yeast: " + request.POST['name'])

    context = {'form': form}
    # TODO: Start here tomorrow, create templates
    return render(request, 'beer_recipes/new_yeast.html', context)


@login_required
def new_misc(request):
    """ Creates a new miscellaneous ingredient """
    if request.method != 'POST':
        form = MiscForm()
    else:
        form = MiscForm(data=request.POST)
        if form.is_valid():
            new_misc = form.save(commit=False)
            new_misc.user = request.user.username
            new_misc.save()
            return my_ingredients(request, message="Successfully created miscellaneous ingredient: " + request.POST['name'])

    context = {'form': form}
    # TODO: Start here tomorrow, create templates
    return render(request, 'beer_recipes/new_misc.html', context)


@login_required
def new_water(request):
    """ Creates a new water profile """
    if request.method != 'POST':
        form = WaterForm()
    else:
        form = WaterForm(data=request.POST)
        if form.is_valid():
            new_water = form.save(commit=False)
            new_water.user = request.user.username
            new_water.save()
            return my_ingredients(request, message="Successfully created water profile: " + request.POST['name'])

    context = {'form': form}
    # TODO: Start here tomorrow, create templates
    return render(request, 'beer_recipes/new_water.html', context)


#  CRUD views here ------------------------------------------------------------
@login_required
def edit_recipe(request, error="", message=""):
    """ Edits information about a specific recipe """
    if request.method == 'GET':
        # create a temp object to store the get info
        temp = request.GET['edit_recipe']
        temp_recipe = BeerRecipe.objects.get(name=temp)
        return render(request, 'beer_recipes/edit_recipe.html', temp_recipe)


class HopUpdate(UpdateView):
    model = Hop
    fields = ['name', 'description', 'alpha', 'time', 'amount', 'use']


class HopDelete(DeleteView):
    model = Hop
    success_url = reverse_lazy('beer_recipes:my_ingredients')


class HopDetails(DetailView):
    model = Hop


class FermentableUpdate(UpdateView):
    model = Fermentable
    fields = ['name', 'description', 'amount', 'ferm_yield', 'color', 'type']


class FermentableDelete(DeleteView):
    model = Fermentable
    success_url = reverse_lazy('beer_recipes:my_ingredients')


class FermentableDetails(DetailView):
    model = Fermentable


class MiscUpdate(UpdateView):
    model = Misc
    fields = ['name', 'description']


class MiscDelete(DeleteView):
    model = Misc
    success_url = reverse_lazy('beer_recipes:my_ingredients')


class MiscDetails(DetailView):
    model = Misc


class WaterUpdate(UpdateView):
    model = Water
    fields = ['name', 'description']


class WaterDelete(DeleteView):
    model = Water
    success_url = reverse_lazy('beer_recipes:my_ingredients')


class WaterDetails(DetailView):
    model = Water


class YeastUpdate(UpdateView):
    model = Yeast
    fields = ['name', 'description']


class YeastDelete(DeleteView):
    model = Yeast


class YeastDetails(DetailView):
    model = Yeast
    success_url = reverse_lazy('beer_recipes:my_ingredients')


class RecipeDetails(DetailView):
    model = BeerRecipe
