from typing import List
import mysql.connector as db
#import constantes
from constantes import DB_HOSTNAME,DB_DATABASE,DB_PASSWORD,DB_USERNAME
import random


def abrir_conexion() -> db.pooling.PooledMySQLConnection | db.MySQLConnection:
    """Abre una conexión con la base de datos

        Deben especificarse los datos en el módulo de constantes para poder
        conectar a la base de datos local correspondiente.

    Returns:
        PooledMySQLConnection | MySQLConnection: conexión a la base de datos
    """
    return db.connect(host=DB_HOSTNAME,
                      user=DB_USERNAME,
                      password=DB_PASSWORD,
                      database=DB_DATABASE)

def consulta_generica(conn : db.MySQLConnection, consulta : str) -> List[db.connection.RowType]:
    """Hace una consulta la base de datos

    Args:
        conn (MySQLConnection): Conexión a la base de datos obtenida por abrir_conexion()
        consulta (str): Consulta en SQL para hacer en la BD

    Returns:
        List[RowType]: Una lista de tuplas donde cada tupla es un registro y 
                        cada elemento de la tupla es un campo del registro.
    """
    cursor = conn.cursor(buffered=True)
    cursor.execute(consulta)
    return cursor.fetchall()

def modificacion_generica(conn : db.MySQLConnection, consulta : str) -> int:
    cursor = conn.cursor(buffered=True)
    cursor.execute(consulta)
    conn.commit()
    return cursor.rowcount

#ej.1
def cargar_usuario (conn : db.MySQLConnection, nombre : str):
    existe_jugador = consulta_generica (f"SELECT COUNT(*) FROM jugadores WHERE nombre = '{nombre}'")
    if existe_jugador()[0][0] > 0:
       raise ValueError(f'El nombre ya existe en la tabla')
    resultado = modificacion_generica(conn, f"INSERT INTO jugadores(nombre) VALUES('{nombre}')")
    tid = consulta_generica(conn, "SELECT id FROM jugadores ORDER BY id DESC LIMIT 1")
    return tid[0][0]

#ej.2
def verificar_existencia (conn : db.MySQLConnection, nombre : str):
    """Verificar si existe un usuario"""
    existe_jugador = consulta_generica (f"SELECT COUNT(*) FROM jugadores WHERE nombre = '{nombre}'")
    if existe_jugador()[0] > 0:
        return True
    return False

#ej.3
def cargar_palabra (conn : db.MySQLConnection, intentos, id_palabras, id_jugador):
    if intentos <0 or intentos > 6: 
        raise ValueError("Cantidad invalida")
    modificacion_generica(conn, f'INSERT INTO wordle.jugadas(palabra, jugador, intentos VALUES({id_palabras},{id_jugador})')
    return consulta_generica(conn, f'SELECT * from wordle.jugadas WHERE palabra= {id_palabras} and jugador= {id_jugador}')

#ej.4 - obtener una lista de los ids de las palabras que ya ha jugado un jugador.
def lista_palabras_jugador (conn : db.MySQLConnection, id_jugador : int) -> List [db.connection.RowType]:
    num_j=consulta_generica(conn, f'SELECT count(id) FROM jugadores WHERE id={id_jugador}')
    if num_j[0][0] == 0:
        raise ValueError(f'No existe el jugador {id_jugador}')
    res= consulta_generica(conn, f'SELECT jugadas.palabra, jugadores.nombre FROM jugadas LEFT JOIN jugadores ON jugadas.jugador = {id_jugador}')
    return res

#ej.5 - obtener una palabra al azar de la tabla palabras que no esté en una lista de ids pasada por parámetro.
def obtener_palabra (conn : db.MySQLConnection, id_jug: int):
    palabras_jugador = lista_palabras_jugador(conn, id_jug)
    id_palabra = random.randint(1,4752)
    for i in palabras_jugador[0]:
        while id_palabra == i:
            id_palabra = random.randint(1, 4752)
        palabra = consulta_generica(conn, f'SELECT palabra FROM palabras WHERE id = {id_palabra}')
    return palabra