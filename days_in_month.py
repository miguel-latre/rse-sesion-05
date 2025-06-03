def is_leap_year(year: int) -> bool:
    """Return whether the argument is a leap year.

    Args:
        year: a year posterior to the adoption of the Gregorian calendar (1582)

    Returns:
        True if the year is leap according to the Gregorian calendar,
        False otherwise.
    """

    multiple_of_4 = year % 4 == 0
    multiple_of_100 = year % 100 == 0
    multiple_of_400 = year % 400 == 0
    return multiple_of_400 or (multiple_of_4 and not multiple_of_100)


def days_in_month(month: int, year: int) -> int:
    """Return the number of days of a month in a certain year.

    Args:
        month: the month we are interested in. Must be in the interval [1, 12].
        year: the year of the month. Must be posterior to 1582.

    Returns:
        the number of days that provided month has in the provided year.
    """
    if month == 2:
        # February: number of days depends on the year
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month in (4, 6, 9, 11):
        # April, June, September, November
        return 30
    else:
        # Rest
        return 31
