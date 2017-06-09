from django import forms

from test_app.models import User


class AddNameForm(forms.Form):
    name = forms.CharField(max_length=20, initial='Enter name, please')

    def clean_name(self):
        name = self.cleaned_data['name']
        if User.objects.filter(name=name).first():
            raise forms.ValidationError("You can't add this name, it %s already exist" % name)
        return name
