from django.contrib import admin
from tree_menu.components.models import Component


class ComponentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'menu')


admin.site.register(Component, ComponentAdmin)
