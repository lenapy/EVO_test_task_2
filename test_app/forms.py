from django import forms

from test_app.models import User


class AddNameForm(forms.Form):
    name = forms.CharField(max_length=20, initial='')

    def clean_name(self):
        name = self.cleaned_data['name']
        if User.objects.filter(name__icontains=name).first():
            raise forms.ValidationError("You can't add this name, %s already exist" % name)
        return name


class DeleteNameForm(forms.Form):
    name = forms.CharField(max_length=20, initial='')

    def clean_name(self):
        name = self.cleaned_data['name']
        if not User.objects.filter(name=name).first():
            raise forms.ValidationError("Name, %s doesn't exist" % name)
        return name
