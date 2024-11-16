from test_data import BunTestData
from praktikum.helper import Mocks

class TestBun:

    def test_bun_init(self, bun):
        assert bun.name == BunTestData.BUN_CORRECT_NAME and bun.price == BunTestData.BUN_CORRECT_PRICE

    def test_bun_get_name(self, bun):
        assert bun.get_name() == Mocks.bun_mock(BunTestData.BUN_CORRECT_DATA).get_name()

    def test_bun_get_price(self, bun):
        assert bun.get_price() == Mocks.bun_mock(BunTestData.BUN_CORRECT_DATA).get_price()

