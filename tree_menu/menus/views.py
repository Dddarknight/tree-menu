from django.views import generic

from tree_menu.menus.models import Menu


class MenuView(generic.ListView):
    template_name = 'index.html'
    model = Menu
