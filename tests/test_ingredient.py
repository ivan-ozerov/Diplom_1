from test_data import IngredientTestData
from praktikum.ingredient import Ingredient
import pytest
from praktikum.helper import Mocks


class TestIngredient:

    @pytest.mark.parametrize(
        "type, name, price",
        [
            IngredientTestData.INGREDIENT_CORRECT_DATA_1,
            IngredientTestData.INGREDIENT_CORRECT_DATA_2,
        ],
    )
    def test_ingredient_init(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.type == type and ingredient.name == name and ingredient.price == price

    def test_ingredient_get_type(self, ingredient):
        assert ingredient.get_type() == Mocks.ingredient_mock(IngredientTestData.INGREDIENT_CORRECT_DATA_1).get_type()

    def test_ingredient_get_name(self, ingredient):
        assert ingredient.get_name() == Mocks.ingredient_mock(IngredientTestData.INGREDIENT_CORRECT_DATA_1).get_name()

    def test_ingredient_get_price(self, ingredient):
        assert ingredient.get_price() == Mocks.ingredient_mock(IngredientTestData.INGREDIENT_CORRECT_DATA_1).get_price()