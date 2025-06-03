import pytest
from qualifications import qualification

"""Session 5 examples (automatic testing)"""


def test_2_is_fail():
    assert qualification(2.5) == "SS"


def test_6_is_pass():
    assert qualification(6) == "AP"


def test_8_is_good():
    assert qualification(8) == "NT"


def test_9_is_outstanding():
    assert qualification(9.5) == "SB"


def test_negative_is_wrong():
    with pytest.raises(ValueError):
        qualification(-1)


def test_more_than_10_is_wrong():
    with pytest.raises(ValueError):
        qualification(11)


def test_more_than_one_decimal_place_is_wrong():
    with pytest.raises(ValueError):
        qualification(4.95)


def test_non_numerical_marks_are_wrong():
    with pytest.raises(TypeError):
        qualification("Non numerical")
