from django.contrib import admin
from tree_menu.menus.models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Menu, MenuAdmin)
