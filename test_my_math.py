import my_math


def test_add():             # konwencja nazwa test_nazwafunkcji
    assert my_math.add(7, 3) == 10
    assert my_math.add(7, -1) == 6
    assert my_math.add(4.3, 5.3) == 9.6

def test_product():
    assert my_math.product(7, 3) == 21
    assert my_math.product(7, -1) == -7
    assert my_math.product(4.3, 5.3) == 22.79

def test_reversal():
    assert my_math.invert_string("tak") == "kat"


def test_palindrom():
    assert my_math.palindrom("ala") == True
    assert my_math.palindrom("as") != True
    assert not my_math.palindrom("as")

test_add()
test_product()
test_reversal()
test_palindrom()
