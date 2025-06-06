from count_letters import count_letter_frequencies

EXPECTED_QUIXOTE = {
    "A": 200495,
    "B": 24147,
    "C": 59436,
    "D": 87237,
    "E": 229189,
    "F": 7581,
    "G": 17225,
    "H": 19920,
    "I": 90075,
    "J": 10530,
    "L": 89141,
    "M": 44658,
    "N": 108441,
    "Ñ": 4241,
    "O": 162514,
    "P": 35465,
    "Q": 32483,
    "R": 100954,
    "S": 125727,
    "T": 61749,
    "U": 79559,
    "V": 17855,
    "W": 2,
    "X": 377,
    "Y": 25115,
    "Z": 6491,
}


def test_frecuencias_quijote():
    assert count_letter_frequencies("res/quijote.txt") == EXPECTED_QUIXOTE
