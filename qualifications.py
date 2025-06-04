"""Session 5 examples (automatic testing)
The function qualification has one defect.
"""


def qualification(mark: float) -> str:
    """Returns the qualitative grade corresponding to the mark.
    Args:
        mark: the numerical score, to the nearest decimal place,
        for which the qualitative score is to be calculated
    Returns:
        The qualitative rating corresponding to the qualification
        numerical mark in accordance with the "Unizar’s Reglamento de
        Normas de Evaluación del Aprendizaje", expressed as "SB", "NT",
        "AP", "SS".
    Raises:
        ValueError: if the mark is not between 0 and 10 or is expressed
        with more than one decimal place.
    """
    if mark < 0 or mark > 10 or round(mark, 1) != mark:
        raise ValueError
    elif mark < 5:
        return "SB"
    elif mark < 7:
        return "AP"
    elif mark < 9:
        return "NT"
    else:
        return "SB"


def main() -> None:
    mark = float(input("Mark: "))
    print(qualification(mark))


if __name__ == "__main__":
    main()
