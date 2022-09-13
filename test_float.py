import pytest
import math

@pytest.mark.parametrize('base, exponent, answer', [
    (2., 5, 32.),
    (-1., 2, 1),
    (0, 0., 1),
    (2, 1/2, math.sqrt(2))
])
def test_pow(base, exponent, answer):
    assert math.isclose(base**exponent, answer)


@pytest.mark.parametrize('a, b, answer', [
    (0., 1/2, 0),
    (10.**10, -0., 0),
    (-2, -0.5, 1)
])
def test_mul(a, b, answer):
    assert math.isclose(a * b, answer)


def test_zero_inf():
    assert math.isnan(math.inf * 0)
