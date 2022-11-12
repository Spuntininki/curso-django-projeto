from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeBaseTest


class RecipeSearchViewTest(RecipeBaseTest):

    def test_if_search_view_is_correct(self):
        view = resolve(reverse('recipes:search'))
        self.assertIs(view.func, views.search)

    def test_if_recipe_search_loads_the_correct_template(self):
        url = reverse('recipes:search') + '?search=Teste'
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_if_recipe_search_raises_404_if_no_input(self):
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_if_search_term_is_on_page_if_not_found(self):
        url = reverse('recipes:search') + '?search=test'
        response = self.client.get(url)
        self.assertIn(
            '<h1>"test" was not Found here </h1>',
            response.content.decode('utf-8')
        )
