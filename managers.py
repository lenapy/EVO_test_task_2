from django.db import models


def capitalize_name(name):
    if not str(name).istitle():
        cap_name = str(name).capitalize()
        return cap_name
    return name


class NameManager(models.Manager):
    def add_name(self, enter_name):  # self - model
        cap_name = capitalize_name(enter_name)
        name = self.create(name=cap_name)
        name.save()
        return name.pk

    def delete_name(self, enter_name):
        cap_name = capitalize_name(enter_name)
        name = self.filter(name=cap_name).first()
        name.delete()
