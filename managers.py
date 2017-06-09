from django.db import models


class UserManager(models.Manager):
    def add_name(self, name):  # self - model
        user = self.create(name=name)
        user.save()
        return user.pk
