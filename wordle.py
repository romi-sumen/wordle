import dbaccess
from typing import List
import mysql.connector as db
#import constantes
from constantes import DB_HOSTNAME,DB_DATABASE,DB_PASSWORD,DB_USERNAME

#a)Verificar si una letra está dentro de una palabra devolviendo una lista 
# con las posiciones donde se encuentra la misma o lista vacía en caso de no encontrarse.

def verificar_letra(palabra : str, letra : chr):
    posiciones = []
    for i in range(len(palabra)):
        if palabra[i] == letra:
            posiciones.append(i)
    return posiciones

#b)Compara dos palabras, devuelve un código (como prefiera hacerlo) que indica si la 
# letra está o no en la palabra y si está en la posición correcta (puede utilizar una lista, 
# un formato de string (str) o cualquier otro recurso que desee). 
# Tenga en cuenta que ahora cuenta con letras repetidas en el diccionario. 

def comparar_palabras (palabra_jugador : str, intento : str):
    resultado = []
    for i in range(len(palabra_jugador)):
        if palabra_jugador [i] == intento[i]: resultado.append('X')
        elif palabra_jugador[i] in intento: resultado.append('O')
        else: resultado.append('_')
        return resultado

#c)Recibe el nombre de un jugador y devuelve una palabra y su id (en formato lista o tupla) 
# que no haya jugado (puede que sea la primera vez que juega o no)