import pytest
from temperature import to_fahrenheit


def test_to_fahrenheit():
    assert to_fahrenheit(30) == 86


def test_to_Fahrenheit_no_numeric():
    with pytest.raises(TypeError):
        to_fahrenheit("thirty")


@pytest.mark.parametrize(
    "celsius, expected", [(30, 86), (0, 32), (37.7777777777777777, 100), (100, 212)]
)
def test_to_fahrenheit_parameterized(celsius, expected):
    assert to_fahrenheit(celsius) == expected


def test_to_fahrenheit_tolerant():
    assert to_fahrenheit(37.8) == pytest.approx(100, abs=1e-1)
