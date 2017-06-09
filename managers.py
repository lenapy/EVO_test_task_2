from django.db import models


class NameManager(models.Manager):
    def add_name(self, enter_name):  # self - model
        name = self.create(name=enter_name)
        name.save()
        return name.pk

    def delete_name(self, enter_name):
        name = self.filter(name=enter_name).first()
        name.delete()
