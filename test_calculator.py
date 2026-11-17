import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Nolga bo'lish mumkin emas"):
        divide(5, 0)


def test_divide_float_numbers():
    assert divide(9, 2) == 4.5


def test_add_invalid_input_raises_error():
    with pytest.raises(TypeError):
        add("2", 3)