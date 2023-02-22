from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from tree_menu.menus.models import Menu


class MenuView(generic.ListView):
    template_name = 'index.html'
    model = Menu
