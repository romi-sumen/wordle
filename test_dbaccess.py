# pylint: disable=missing-function-docstring
import pytest
import dbaccess
from constantes import DB_TABLES

def test_abrir_conexion_existe():
    at_dbaccess = dir(dbaccess)
    assert 'abrir_conexion' in at_dbaccess
    
@pytest.fixture
def conn_fixture():
    pytest.dbconn = dbaccess.abrir_conexion()

def test_abrir_conexion(conn_fixture):
    conn = pytest.dbconn
    assert conn

@pytest.mark.usefixtures("conn_fixture")
@pytest.mark.parametrize('tabla', DB_TABLES)
def test_chequear_tabla(tabla):
    resultado = dbaccess.consulta_generica(pytest.dbconn, f"SHOW TABLES LIKE '{tabla}'")
    assert len(resultado) == 1
    
def test_consulta_generica_existe():
    at_dbaccess = dir(dbaccess)
    assert 'consulta_generica' in at_dbaccess
           
def test_modificacion_generica_existe():
    at_dbaccess = dir(dbaccess)
    assert 'modificacion_generica' in at_dbaccess
    
def test_cargar_usuario_existe():
    at_dbaccess = dir(dbaccess)
    assert 'cargar_usuario' in at_dbaccess
    
def test_verificar_existencia():
    at_dbaccess = dir(dbaccess)
    assert 'verificar_existencia' in at_dbaccess
    
def test_lista_palabras_jugador_existe():
    at_dbaccess = dir(dbaccess)
    assert 'lista_palabras_jugador' in at_dbaccess
    
@pytest.mark.usefixtures("conn_fixture")
def lista_palabras_jugador():
    resultado = dbaccess.lista_palabras_jugador(pytest.dbconn, 1)
    assert resultado[0] == (4, 'abada')

@pytest.mark.usefixtures("conn_fixture")    
def test_lista_palabras_jugador_existente():
    with pytest.raises (ValueError) as ex_info:
        dbaccess.lista_palabras_jugador(pytest.dbconn, -4)
    assert str(ex_info.value) == f'No existe el jugador {-4}'
    
#@pytest.mark.usefixtures("conn_fixture") 
#def test_obtener_palabra():
#    resultado = dbaccess.obtener_palabra(pytest.dbconn, 1)
#    id_palabra = dbaccess.consulta_generica(pytest.dbconn, f"SELECT id FROM palabras WHERE palabra = '{resultado[0][0]}")
#    esperado = dbaccess.consulta_generica(pytest.dbconn, f'SELECT palabra FROM palabras WHERE id = {id_palabra[0][0]}')
#    assert resultado[0] == esperado[0]
    
def pytest_sessionfinish(session, status):
    # pylint: disable=unused-argument
    pytest.dbconn.close()
