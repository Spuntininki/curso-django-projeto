from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views


# Classe para teste
class RecipeURLsTest(TestCase):
    def test_if_recipes_home_url_is_correct(self):
        url_input = reverse('recipes:home')
        self.assertEqual(url_input, '/')

    def test_if_recipes_category_url_is_correct(self):
        url_input = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url_input, '/recipes/category/1/')

    def test_if_recipes_detail_url_is_correct(self):
        url_input = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url_input, '/recipes/1/')


class RecipeViewTest(TestCase):
    def test_if_home_view_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_if_category_view_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)

    def test_if_detail_page_recipe_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)
