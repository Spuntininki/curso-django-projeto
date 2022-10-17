from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import RecipeBaseTest


class TestRecipeModel(RecipeBaseTest):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()

        return super().setUp()

    @parameterized.expand(
        [
            ('title',  65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65)
        ]

    )
    def test_if_recipe_fields_exceds_max_lenght_raises_exception(
            self,
            atribute,
            max_lenght):
        setattr(self.recipe, atribute, 'A' * (max_lenght + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_if_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_default_recipe_class()
        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg='failed because preparation_steps_is_html is not False'
        )

    def test_if_recipe_is_published_is_false_by_default(self):
        recipe = self.make_default_recipe_class()
        self.assertFalse(
            recipe.is_published,
            msg='failed because is_published is not False'
        )

    def test_recipe_str_representation(self):
        needed = 'Recipe Str Representation test'
        self.recipe.title = needed
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
            str(self.recipe),
            needed,
            msg='the str represetentation must be the recipe title.'
        )
