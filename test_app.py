from app import add, invert_string


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_invert_string():
    assert invert_string("abc") == "cba"
    assert invert_string("") == ""
