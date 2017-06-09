from django.shortcuts import render, redirect

from test_app.models import User
from test_app.forms import AddNameForm


def add_name(request):
    if request.method == 'POST':
        form = AddNameForm(data=request.POST)
        if form.is_valid():
            if not User.objects.add_name(
                    form.cleaned_data['name'],
            ):
                pass
            return redirect('user:login')
    else:
        form = AddNameForm()
    return render(request, 'add_name.html',
                  context={'form': form})


def delete_name():
    pass

