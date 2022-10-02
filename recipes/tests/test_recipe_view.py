from unittest import skip

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

    def test_if_recipe_home_loads_correct_template(self):
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


class RecipeCategoryViewTest(RecipeBaseTest):

    def test_if_recipe_category_is_published_equal_False_is_working(self):
        recipe = self.make_recipe(is_published=False)

        respose = self.client.get(
            reverse('recipes:category', kwargs={'category_id': recipe.category.id}))

        self.assertEqual(respose.status_code, 404)

    def test_if_category_template_loads_recipes(self):
        required_title = 'This title is for a template test'
        self.make_recipe(title=required_title)
        response = self.client.get(
            reverse(
                'recipes:category', kwargs={'category_id': 1}
            )
        )
        response_content_recipe = response.content.decode('utf-8')

        self.assertIn(required_title, response_content_recipe)

    def test_if_category_view_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)

    def test_if_recipe_category_returns_404_when_no_category(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)


class RecipeDetailViewTest(RecipeBaseTest):

    def test_if_view_recipes_is_published_equal_False_is_working(self):
        recipe = self.make_recipe(is_published=False)

        respose = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.category.id}))

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
