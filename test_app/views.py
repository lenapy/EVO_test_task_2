from django.shortcuts import render, redirect
import random
from django.http import JsonResponse

from test_app.models import User
from test_app.forms import AddNameForm, DeleteNameForm


def index(request):
    return redirect('main')


def main(request):
    return render(request, 'main.html')


def add_name(request):
    if request.method == 'POST':
        form = AddNameForm(data=request.POST)
        if form.is_valid():
                User.objects.add_name(form.cleaned_data['name'])
                return JsonResponse({'result': True})
        else:
            return JsonResponse({'result': False, 'errors': form.errors})
    else:
        form = AddNameForm()
    return render(request, 'main.html',
                  context={'form': form})


def delete_name(request):
    if request.method == 'POST':
        form = DeleteNameForm(data=request.POST)
        if form.is_valid():
            User.objects.delete_name(form.cleaned_data['name'])
            return JsonResponse({'result': True})
        else:
            return JsonResponse({'result': False, 'errors': form.errors})
    else:
        form = DeleteNameForm()
    return render(request, 'main.html',
                  context={'form': form})


def get_random_names(request):
    names_dict = User.objects.values('name').order_by('?')[:3]  # queries may be expensive and slow
    names_list = []
    for names_data in names_dict:
        names_list.append(names_data['name'])
    return JsonResponse({'result': True, 'names': names_list})


def get_random_names_variant_2(request):
    count = User.objects.count()
    names_list = []
    while len(names_list) < 3:
        name_id = random.randint(1, count)
        name = User.objects.filter(id=name_id).first()
        if name:
            names_list.append(name)
    return JsonResponse({'result': True, 'names': names_list})


def get_random_names_variant_3(request):
    names_list = random.sample(list(User.objects.values_list('name')), 3)
    return JsonResponse({'result': True, 'names': names_list})
