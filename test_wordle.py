# pylint: disable=missing-function-docstring
import pytest
import dbaccess
import wordle
from constantes import DB_TABLES

def test_verificar_letra_existe():
    at_wordle = dir(wordle)
    assert 'verificar_letra' in at_wordle
    
@pytest.mark.usefixtures("conn_fixture")
def test_verificar_letra_resultado():
    resultado = wordle.verificar_letra(pytest.dbconn, 1)
    assert resultado[1] == ("c", "abaca")