"""Ejercicio 3
   
   Quiere contar las letras del Quijote, pero hay dos defectos.
"""

import string
from typing import Final

NO_LETRAS: Final = string.punctuation + string.whitespace + string.digits + "¿¡«»"


def frecuencias(file_name: str) -> dict[str, int]:
    """Devuelve un diccionario con las apariciones de cada letra en file_name

    Args:
        file_name: el fichero cuyo contenido se analizará

    Returns:
        Un diccionario con las frecuencias absolutas de aparición de cada
        letra del alfabeto español en el file_name.

    Rises:
        OSError si file_name no existe o no puede abrirse.
    """
    resultado = {}
    with open(file_name, encoding="utf-8") as file:
        for linea in file:
            procesar_linea(linea, resultado)
    return resultado


def procesar_linea(linea: str, resultado: dict[str, int]) -> None:
    linea = linea.translate(str.maketrans("ÁÉÍÓÚÚÏÀÙ", "AEIOUUIAU", NO_LETRAS))
    for letra in linea:
        resultado[letra] = resultado.get(letra, 0) + 1


print(frecuencias("session-2/res/quijote.txt"))
