import math

import pytest

from calculator import add, ln, log, sub


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(10, 4) == 6


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
