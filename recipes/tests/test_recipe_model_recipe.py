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
