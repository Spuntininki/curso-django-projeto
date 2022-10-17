from django.core.exceptions import ValidationError

from .test_recipe_base import RecipeBaseTest


class TestCategoryModel(RecipeBaseTest):
    def setUp(self) -> None:
        self.category = self.make_category()

        return super().setUp()

    def test_category_name_max_lenght(self):
        max_lenght = 65
        self.category.name = 'A' * (max_lenght + 1)
        with self.assertRaises(ValidationError, msg='need to verify the max_lenght atribute in models.py, because the expected max lenght was 65'):
            self.category.full_clean()

    def test_category_str_representation(self):
        self.assertEqual(
            str(self.category),
            self.category.name,
            msg='the str representation must be category name'
        )
