from django.test import TestCase
from django.urls import reverse


# Classe para teste
class RecipeURLsTest(TestCase):
    def test_if_url_is_correct(self):
        url_input = reverse('recipes:home')
        self.assertEqual(url_input, '/')
