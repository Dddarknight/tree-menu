from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from tree_menu.components import views

urlpatterns = [
    path(
        'menus/<int:menu_pk>/components/<int:component_pk>',
        views.MenuComponentsView.as_view(),
        name='tree'
    ),
]
