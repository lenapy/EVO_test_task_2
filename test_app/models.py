from django.db import models
from django.contrib import admin

from managers import NameManager


class User(models.Model):
    name = models.CharField(max_length=20)

    objects = NameManager()

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name

admin.site.register(User)
