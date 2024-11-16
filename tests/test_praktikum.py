from praktikum import praktikum

class TestPraktikum:

    def test_praktikum(self, capsys):
        praktikum.main()
        out = capsys.readouterr()
        expected_out = "(==== black bun ====)\n= sauce sour cream =\n= filling cutlet =\n= filling dinosaur =\n(==== black bun ====)\n\nPrice: 700\n"
        print(expected_out)
        print(out[0])
        assert out[0] == expected_out