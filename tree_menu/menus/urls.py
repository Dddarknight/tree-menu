from django.urls import path
from tree_menu.menus import views


urlpatterns = [
    path('', views.MenuView.as_view(), name='menus'),
]
