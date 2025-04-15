import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 5) == -5

def test_multiply(calc):
    assert calc.multiply(4, 3) == 12
    assert calc.multiply(-1, 5) == -5

def test_divide(calc):
    assert calc.divide(10, 2) == 5
    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_modulus(calc):
    assert calc.modulus(10, 3) == 1
    assert calc.modulus(10, 5) == 0
    with pytest.raises(ValueError):
        calc.modulus(10, 0)

def test_power(calc):
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
    assert calc.power(0, 5) == 0

def test_square_root(calc):
    assert calc.square_root(16) == 4
    assert calc.square_root(0) == 0
    with pytest.raises(ValueError):
        calc.square_root(-1)

def test_factorial(calc):
    assert calc.factorial(5) == 120
    assert calc.factorial(0) == 1
    with pytest.raises(ValueError):
        calc.factorial(-5)