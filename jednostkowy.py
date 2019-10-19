def add(x,y):
    return x + y

def product(a,b):
    return a * b

def test_add():             # konwencja nazwa test_nazwafunkcji
    assert add(7, 3) == 10
    assert add(7, -1) == 6
    assert add(4.3, 5.3) == 9.6

def test_product():
    assert product(7, 3) == 21
    assert product(7, -1) == -7
    assert product(4.3, 5.3) == 22.79

test_add()
test_product()

