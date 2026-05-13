import math

import pytest

from calculator import add, divide, ln, log, multiply, power, sqrt, sub


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0


def test_divide():
    assert divide(10, 4) == 2.5
    assert divide(20, 2) == 10


def test_power():
    assert power(4, 2) == 16
    assert power(3, 3) == 27


def test_ln():
    assert ln(math.e) == pytest.approx(1)


def test_log_default_base_10():
    assert log(100) == pytest.approx(2)


def test_log_custom_base():
    assert log(8, 2) == pytest.approx(3)


def test_logarithms_reject_invalid_values():
    with pytest.raises(ValueError):
        ln(0)
    with pytest.raises(ValueError):
        log(-10)
    with pytest.raises(ValueError):
        log(10, 1)


def test_sqrt():
    assert sqrt(4) == 2
