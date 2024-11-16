from test_data import BunTestData
from test_data import IngredientTestData
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database
import pytest

@pytest.fixture
def bun():
    return Bun(*BunTestData.BUN_CORRECT_DATA)


@pytest.fixture
def ingredient():
    return Ingredient(*IngredientTestData.INGREDIENT_CORRECT_DATA_1)


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def database():
    return Database()