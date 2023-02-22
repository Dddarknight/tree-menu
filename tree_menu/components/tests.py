from django.test import Client
from django.test import TestCase
from django.urls import reverse_lazy

from tree_menu.components.models import Component
from tree_menu.menus.models import Menu


class MenuTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.menu1 = Menu.objects.create(name='menu_digits')
        cls.menu2 = Menu.objects.create(name='menu_chars')
        cls.component1_1 = Component.objects.create(
            name='name1', menu=cls.menu1)
        cls.component1_2 = Component.objects.create(
            name='name2', menu=cls.menu1)
        cls.component1_11 = Component.objects.create(
            name='name11', parent=cls.component1_1, menu=cls.menu1)
        cls.component1_12 = Component.objects.create(
            name='name12', parent=cls.component1_1, menu=cls.menu1)
        cls.component1_21 = Component.objects.create(
            name='name21', parent=cls.component1_2, menu=cls.menu1)
        cls.component1_22 = Component.objects.create(
            name='name22', parent=cls.component1_2, menu=cls.menu1)
        cls.component2_a = Component.objects.create(
            name='name_a', menu=cls.menu2)
        cls.component2_b = Component.objects.create(
            name='name_b', menu=cls.menu2)

    def test_menu(self):
        c = Client()
        menu_pk = self.menu1.pk
        component_pk = self.component1_22.pk
        response = c.get(
            reverse_lazy(
                'tree',
                kwargs={'menu_pk': menu_pk, 'component_pk': component_pk}
            )
        )
        self.assertContains(response, self.component1_2.name)
        self.assertContains(response, self.component1_21.name)
        self.assertContains(response, self.component1_22.name)
        self.assertNotContains(response, self.component1_11.name)
        self.assertNotContains(response, self.component1_12.name)
        self.assertNotContains(response, self.component2_a.name)
        self.assertNotContains(response, self.component2_b.name)
