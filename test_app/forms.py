from django import forms

from test_app.models import User

from managers import capitalize_name


class AddNameForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=20, initial='')

    def clean_name(self):
        name = self.cleaned_data['name']
        cap_name = capitalize_name(name)
        if User.objects.filter(name=cap_name).first():
            raise forms.ValidationError("Имя %s, уже добавлено" % name)
        return name


class DeleteNameForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=20, initial='')

    def clean_name(self):
        name = self.cleaned_data['name']
        cap_name = capitalize_name(name)
        if not User.objects.filter(name=cap_name).first():
            raise forms.ValidationError("Имя %s, не было добавлено" % name)
        return name
