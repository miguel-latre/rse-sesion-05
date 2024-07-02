"""Ejercicio sesión 5 (pruebas automáticas)
   Hay un defecto.
"""


def calificacion_cualitativa(nota: float) -> str:
    """Devuelve la calificación cualitativa correspondiente a nota.

    Args:
        nota: la calificación numérica, con la precisión de un decimal, de la
            que se quiere calcular la calificación cualitativa

    Returns:
        La calificación cualitativa correspondiente a la calificación numérica
        nota de acuerdo con el «Reglamento de Normas de Evaluación del
        Aprendizaje» de Unizar, expresada como "SB", "NT", "AP", "SS"

    Raises:
        ValueError: si la calificación no está entre 0 y 10 o tiene más de un
        decimal
    """
    if nota < 0 or nota > 10 or round(nota, 1) != nota:
        raise ValueError
    elif nota < 5:
        return "SB"
    elif nota < 7:
        return "AP"
    elif nota < 9:
        return "NT"
    else:
        return "SB"


def main() -> None:
    nota = float(input("Nota: "))
    print(calificacion_cualitativa(nota))


if __name__ == "__main__":
    main()
