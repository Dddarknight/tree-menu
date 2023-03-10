from django.views import generic
from django.shortcuts import render

from tree_menu.components.utils import build_tree


class MenuComponentsView(generic.TemplateView):
    template_name = 'components/menu-components.html'

    def get(self, request, *args, **kwargs):
        component_pk = kwargs.get('component_pk')
        menu_pk = kwargs.get('menu_pk')
        tree = build_tree(component_pk, menu_pk)
        context = {'tree': tree}
        return render(request, self.template_name, context)
