from django.db import models

from tree_menu.menus.models import Menu


class Component(models.Model):
    name = models.CharField(
        max_length=20, null=False, blank=False, unique=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL)
    menu = models.ForeignKey(
        Menu, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
