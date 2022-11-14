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

        response = self.client.get(url)
        self.assertIn(
            '<h1>"test" was not Found here </h1>',
            response.content.decode('utf-8')
        )

    def test_if_search_query_is_working_propely_with_title_as_param(self):
        title1 = 'This is recipe one'
        title2 = 'This is recipe two'

        recipe1 = RecipeBaseTest.make_recipe(
            self,
            slug='one',
            title=title1,
            author_data={'username': 'user_one'}
        )
        recipe2 = RecipeBaseTest.make_recipe(
            self,
            slug='two',
            title=title2,
            author_data={'username': 'user_two'}
        )
        response1 = self.client.get(
            reverse('recipes:search') + f'?search={title1}'
        )
        response2 = self.client.get(
            reverse('recipes:search') + f'?search={title2}'
        )
        response_both = self.client.get(
            reverse('recipes:search') + '?search=this is'
        )

        self.assertIn(recipe1, response1.context['recipes'])
        self.assertNotIn(recipe2, response1.context['recipes'])

        self.assertIn(recipe2, response2.context['recipes'])
        self.assertNotIn(recipe1, response2.context['recipes'])

        self.assertIn(recipe1, response_both.context['recipes'])
        self.assertIn(recipe2, response_both.context['recipes'])

    def test_if_search_query_is_working_propely_with_description_as_param(self):
        title1 = 'This is recipe one'
        title2 = 'This is recipe two'
        description_1 = 'Essa aqui é a primeira receita'
        description_2 = 'Essa aqui é a segunda receita'

        recipe1 = RecipeBaseTest.make_recipe(
            self,
            slug='one',
            title=title1,
            description=description_1,
            author_data={'username': 'user_one'}
        )
        recipe2 = RecipeBaseTest.make_recipe(
            self,
            slug='two',
            title=title2,
            description=description_2,
            author_data={'username': 'user_two'}
        )
        response1 = self.client.get(
            reverse('recipes:search') + f'?search={description_1}'
        )
        response2 = self.client.get(
            reverse('recipes:search') + f'?search={description_2}'
        )
        response_both = self.client.get(
            reverse('recipes:search') + '?search=Essa aqui é a'
        )

        self.assertIn(recipe1, response1.context['recipes'])
        self.assertNotIn(recipe2, response1.context['recipes'])

        self.assertIn(recipe2, response2.context['recipes'])
        self.assertNotIn(recipe1, response2.context['recipes'])

        self.assertIn(recipe1, response_both.context['recipes'])
        self.assertIn(recipe2, response_both.context['recipes'])
