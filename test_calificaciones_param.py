import pytest
from calificaciones import calificacion_cualitativa

"""Ejemplos sesión 5 (pruebas automáticas)"""


@pytest.mark.parametrize("nota, esperado",
                         [(2.5, "SS"), (6, "AP"), (8, "NT"), (9.5, "SB")])
def test_calificaciones_validas(nota, esperado):
    assert calificacion_cualitativa(nota) == esperado


@pytest.mark.parametrize("nota", [-1, 11, 4.95])
def test_calificaciones_no_validas(nota):
    with pytest.raises(ValueError):
        calificacion_cualitativa(nota)


def test_calificaciones_no_numericas():
    with pytest.raises(TypeError):
        calificacion_cualitativa("No numérico")
