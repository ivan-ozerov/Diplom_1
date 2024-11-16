import praktikum.ingredient_types as ingredient_types
from unittest.mock import Mock
from test_data import IngredientTestData

class Mocks:

    @staticmethod
    def ingredient_mock(test_data):
        ingredient_mock = Mock()
        attrs = {'type': test_data[0], 
                'name': test_data[1], 
                'price': test_data[2], 
                'get_type.return_value': test_data[0],
                'get_name.return_value': test_data[1],
                'get_price.return_value': test_data[2]}
        ingredient_mock.configure_mock(**attrs)
        return ingredient_mock

    @staticmethod
    def bun_mock(test_data):        
        bun_mock = Mock()
        attrs = {'name': test_data[0], 
                'price': test_data[1], 
                'get_name.return_value': test_data[0],
                'get_price.return_value': test_data[1]}
        bun_mock.configure_mock(**attrs)
        return bun_mock
