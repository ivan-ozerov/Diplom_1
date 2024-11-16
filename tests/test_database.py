class TestDatabase:

    def test_database_init(self, database):
        assert len(database.buns) == 3 and len(database.ingredients) == 6

    def test_available_buns(self, database):
        assert len(database.available_buns()) == 3

    def test_available_ingredients(self, database):
        assert len(database.available_ingredients()) == 6
