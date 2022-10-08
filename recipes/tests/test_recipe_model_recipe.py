from django.core.exceptions import ValidationError

from .test_recipe_base import RecipeBaseTest


class TestRecipeModel(RecipeBaseTest):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()

        return super().setUp()

    def test_if_recipe_title_exceds_65_chars_raises_exception(self):
        self.recipe.title = 'A' * 70

        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
