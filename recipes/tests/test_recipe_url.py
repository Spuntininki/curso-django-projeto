from django.test import TestCase
from django.urls import reverse


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
