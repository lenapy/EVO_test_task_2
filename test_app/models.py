from django.db import models
from django.contrib import admin


class User(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name

admin.site.register(User)
