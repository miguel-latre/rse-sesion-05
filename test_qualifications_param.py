import pytest
from qualifications import qualification

"""Session 5 examples (automatic testing)"""


@pytest.mark.parametrize(
    "mark, expected", [(2.5, "SS"), (6, "AP"), (8, "NT"), (9.5, "SB")]
)
def test_valid_qualifications(mark: float, expected: str):
    assert qualification(mark) == expected


@pytest.mark.parametrize("mark", [-1, 11, 4.95])
def test_non_valid_qualifications(mark: float):
    with pytest.raises(ValueError):
        qualification(mark)


def test_non_numeric_qualifications():
    with pytest.raises(TypeError):
        qualification("Non numerical")
