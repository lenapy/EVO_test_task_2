from django.shortcuts import render, redirect
import random

from test_app.models import User
from test_app.forms import AddNameForm, DeleteNameForm


def add_name(request):
    if request.method == 'POST':
        form = AddNameForm(data=request.POST)
        if form.is_valid():
            if not User.objects.add_name(
                    form.cleaned_data['name'],
            ):
                pass
            return render(request, 'success.html')
    else:
        form = AddNameForm()
    return render(request, 'add_name.html',
                  context={'form': form})


def delete_name(request):
    if request.method == 'POST':
        form = DeleteNameForm(data=request.POST)
        if form.is_valid():
            if not User.objects.delete_name(
                    form.cleaned_data['name'],
            ):
                pass
            return render(request, 'success.html')
    else:
        form = DeleteNameForm()
    return render(request, 'delete_name.html',
                  context={'form': form})


def get_random_names(request):
    names_list = random.sample(list(User.objects.values_list('name')), 3)
    count = User.objects.count()

    n = User.objects.order_by('?')[:3]

    names = []
    while len(names) < 3:
        name_id = random.randint(1, count)
        name = User.objects.filter(id=name_id).first()
        if name:
            names.append(name)

    return render(request, 'get_names.html',
                  {'names_list': names_list,
                   'count': count,
                   'names': names,
                   'n': n})
