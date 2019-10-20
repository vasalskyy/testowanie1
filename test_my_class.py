import math         # na samej górze dajemy bloki bibliotek które są standardowo
import pytest       # drugi z importami które trzeba zainstalować
import my_class     # trzeci blok to sa importy wewnętrzne

def test_dog_initialization():
    d = my_class.Dog("Azor")
    assert d.name == "Azor"


def test_dog_speak():
    d = my_class.Dog("Azor")
    assert d.speak() == "hau-hau. Jestem Azor"

def test_lamp_initialization():
    l = my_class.Lamp(True)


@pytest.fixture         # dodaliśmy dekorator fixture, i teraz przy każdej funkcji mogę go użyć jako "c" , biblioteka pytest
def calc():                # tutaj stworzyliśmy fixture
    calc = my_class.Calc()
    return calc

@pytest.mark.parametrize('num1, num2, res',             #jeden string rozdzielony przecinkami jako parametru
                         [(5, 10, 15),                  # tutaj sobie wpisuje parametry do podstawienia
                          (0, 0, 0),
                          (-3, -7, -10),
                          ("ab", "cd", "abcd"),
                          ("", "", "")
                          ])
def test_calc_add_integer_and_string(num1, num2, res, calc):
    assert calc.add(num1, num2) == res

def test_calc_add_float(calc):
    assert pytest.approx(calc.add(5.2, 5.2), 0.0001) == 10.4 # asercja
    assert pytest.approx(calc.add(4.23, -2.1), 0.0001) == 2.13 # błąd związany z niedokładnością floatów dlatego approax

def test_circle_area():
    assert pytest.approx(my_class.circle_area(1), 0.001) == math.pi
    assert my_class.circle_area(0) == 0
    assert my_class.circle_area(2.1) == math.pi * (2.1**2)

def test_area_value_exceptions():
    with pytest.raises(ValueError):
        my_class.circle_area(-3)

def test_area_type_exception(): # ten test przejdzie tylko wtedy gdy wszystkie asercje wyrzucą wyjątek
    with pytest.raises(TypeError):
        my_class.circle_area(3 + 5j)
        my_class.circle_area(True)
        my_class.circle_area("radius")

