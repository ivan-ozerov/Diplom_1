from praktikum.burger import Burger
from praktikum.burger import Ingredient
from praktikum.burger import Bun
from test_data import IngredientTestData
from praktikum.helper import Mocks
from test_data import BunTestData

class TestBurger:

    def test_burger_init(self, burger: Burger):
        assert burger.bun is None and len(burger.ingredients) == 0

    def test_set_buns(self, burger: Burger):
        bun_mock = Mocks.bun_mock(BunTestData.BUN_CORRECT_DATA)
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self, burger: Burger):
        ingredient_mock = Mocks.ingredient_mock(IngredientTestData.INGREDIENT_CORRECT_DATA_1)
        burger.add_ingredient(ingredient_mock)
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == ingredient_mock

    def test_remove_ingredient(self, burger: Burger):
        bun_mock = Mocks.bun_mock(BunTestData.BUN_CORRECT_DATA)
        burger.add_ingredient(bun_mock)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger: Burger):
        mock_ingredient1 = Mocks.ingredient_mock(IngredientTestData.INGREDIENT_CORRECT_DATA_1)
        mock_ingredient2 = Mocks.ingredient_mock(IngredientTestData.INGREDIENT_CORRECT_DATA_2)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(0, 1)
        print(mock_ingredient1)
        print(mock_ingredient2)
        assert len(burger.ingredients) == 2 and burger.ingredients[0].get_name() == mock_ingredient2.get_name() and burger.ingredients[1].get_name() == mock_ingredient1.get_name()

    def test_get_price(self, burger: Burger, bun: Bun):
        mock_ingredient1 = Mocks.ingredient_mock(IngredientTestData.INGREDIENT_CORRECT_DATA_1)
        mock_ingredient2 = Mocks.ingredient_mock(IngredientTestData.INGREDIENT_CORRECT_DATA_2)
        burger.set_buns(bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        sum = mock_ingredient1.get_price() + mock_ingredient2.get_price() + bun.get_price()*2
        assert burger.get_price() == sum

    def test_get_receipt(self, burger: Burger, bun: Bun):
        mock_ingredient1 = Mocks.ingredient_mock(IngredientTestData.INGREDIENT_CORRECT_DATA_1)
        mock_ingredient2 = Mocks.ingredient_mock(IngredientTestData.INGREDIENT_CORRECT_DATA_2)
        burger.set_buns(bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        sum = mock_ingredient1.get_price() + mock_ingredient2.get_price() + bun.get_price()*2
        assert burger.get_receipt() == f'(==== saturn bun ====)\n= sauce milky way sauce =\n= filling mars volcano lava =\n(==== saturn bun ====)\n\nPrice: {sum}'