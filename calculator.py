from numbers import Real

__all__ = ["add", "subtract", "multiply", "divide"]


def _ensure_number(value, name):
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{name} must be a real number")


def add(a, b):
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a + b


def subtract(a, b):
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a - b


def multiply(a, b):
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a * b


def divide(a, b):
    _ensure_number(a, "a")
    _ensure_number(b, "b")

    if b == 0:
        raise ValueError("Nolga bo'lish mumkin emas")
    return a / b