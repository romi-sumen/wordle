# pylint: disable=missing-function-docstring
import pytest
import dbaccess
import wordle
from constantes import DB_TABLES

def test_verificar_letra_existe():
    at_wordle = dir(wordle)
    assert 'verificar_letra' in at_wordle

#def test_verificar_letra_resultado():
#    resultado = wordle.verificar_letra("abaca", "c")
#    estimado = [3]
#    assert resultado == estimado

def test_verificar_comparar_palabras_existe():
    at_wordle = dir(wordle)
    assert 'comparar_palabras' in  at_wordle