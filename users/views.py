from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserForm

# Create your views here.


def register(request):
    """ Register a new user """

    registered = False
    if request.method != 'POST':
        form = UserForm()

    else:
        form = UserForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            registered = True
            return redirect('wine_recipes:index')

        else:
            print(form.errors)
    context = {'form': form, 'registered': registered}
    return render(request, 'users/register.html', context)
