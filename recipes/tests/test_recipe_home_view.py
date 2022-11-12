from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeBaseTest


class RecipeHomeViewTest(RecipeBaseTest):
    def test_if_home_view_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_if_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_if_recipe_home_loads_the_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_home_view_is_showing_recipe_not_found_if_no_recipe(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('<h1>No recipes found here 🥲</h1>',
                      response.content.decode('utf-8'))

    def test_if_recipe_home_is_published_equal_False_is_working(self):
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))

        self.assertIn(
            '<h1>No recipes found here 🥲</h1>',
            response.content.decode('utf-8')
        )

    # @skip"WIP" significa "WORK IN PROGRESS"

    def test_if_home_template_loads_recipes(self):
        self.make_recipe(preparation_time=5)
        response = self.client.get(reverse('recipes:home'))
        response_content_recipe = response.content.decode('utf-8')

        self.assertEqual(len(response.context['recipes']), 1)
        self.assertIn('Recipe Title', response_content_recipe)
        self.assertIn('5 Minutos', response_content_recipe)
        self.assertIn('5 Porções', response_content_recipe)
