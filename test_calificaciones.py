import pytest
from calificaciones import calificacion_cualitativa

"""Ejemplos sesión 5 (pruebas automáticas)"""


def test_2_es_suspenso():
    assert calificacion_cualitativa(2.5) == "SS"


def test_6_es_aprobado():
    assert calificacion_cualitativa(6) == "AP"


def test_8_es_notable():
    assert calificacion_cualitativa(8) == "NT"


def test_9_es_sobresaliente():
    assert calificacion_cualitativa(9.5) == "SB"


def test_negativo_es_error():
    with pytest.raises(ValueError):
        calificacion_cualitativa(-1)


def test_mas_de_10_es_error():
    with pytest.raises(ValueError):
        calificacion_cualitativa(11)


def test_mas_de_un_decimal_es_error():
    with pytest.raises(ValueError):
        calificacion_cualitativa(4.95)


def test_calificaciones_no_validas():
    with pytest.raises(TypeError):
        calificacion_cualitativa("No numérico")
