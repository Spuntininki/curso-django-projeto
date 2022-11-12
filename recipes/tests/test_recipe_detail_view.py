from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeBaseTest


class RecipeDetailViewTest(RecipeBaseTest):

    def test_if_view_recipes_is_published_equal_False_is_working(self):
        recipe = self.make_recipe(is_published=False)

        respose = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.id}))

        self.assertEqual(respose.status_code, 404)

    def test_if_detail_page_recipe_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)

    def test_if_recipes_recipe_returns_404_when_no_recipe(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_if_recipe_template_loads_recipes(self):
        required_title = 'This title is for a template test'
        self.make_recipe(title=required_title)
        response = self.client.get(
            reverse(
                'recipes:recipe', kwargs={'id': 1}
            )
        )
        response_content_recipe = response.content.decode('utf-8')

        self.assertIn(required_title, response_content_recipe)
