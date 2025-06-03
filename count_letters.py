import string
from typing import Final

NON_LETTER_CHARACTERS: Final = (
    string.punctuation + string.whitespace + string.digits + "¿¡«»"
)


def count_letter_frequencies(file_name: str) -> dict[str, int]:
    """Returns a dictionary with the occurrences of each letter in file_name

    Args:
        file_name: the file whose content will be analyzed

    Returns:
        A dictionary with the absolute frequencies of each letter
        of the Spanish alphabet in the file_name.

    Raises:
        OSError if file_name does not exist or cannot be opened.
    """
    result: dict[str, int] = {}
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            process_line(line, result)
    return result


def process_line(line: str, result: dict[str, int]) -> None:
    line = line.upper().translate(
        str.maketrans("ÁÉÍÓÚÚÏÀÙ", "AEIOUUIAU", NON_LETTER_CHARACTERS)
    )
    for character in line:
        result[character] = result.get(character, 0) + 1


print(count_letter_frequencies("res/quixote.txt"))
