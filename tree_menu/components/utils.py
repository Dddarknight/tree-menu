from tree_menu.components.models import Component


def build_tree(component_pk, menu_pk):
    components = Component.objects.filter(menu__pk=menu_pk).select_related(
        'parent').values('id', 'name', 'parent__id', 'menu__id')
    component_dict = {
        node.get('id'): node for node in components}

    if not component_pk:
        for component in components:
            if component.get('parent__id') is None:
                pivot_component = component
                break
    else:
        pivot_component = component_dict.get(component_pk)

    checked_component = pivot_component
    parents_list = [pivot_component]
    while checked_component.get('parent__id') is not None:
        parent = component_dict.get(checked_component.get('parent__id'))
        parents_list.insert(0, parent)
        checked_component = parent

    def inner(parent, parents_list, components):
        node = []
        for component in components:
            if (parent is None and component.get('parent__id') is None) or (
                    parent and component.get(
                        'parent__id') == parent.get('id')):
                if component in parents_list:
                    node.append({
                        'id': component.get('id'),
                        'name': component.get('name'),
                        'menu__id': component.get('menu__id'),
                        'children': inner(
                            component, parents_list, components)
                    })
                else:
                    node.append({
                        'id': component.get('id'),
                        'name': component.get('name'),
                        'menu__id': component.get('menu__id'),
                        'children': []
                    })
        return node

    return inner(None, parents_list, components)
