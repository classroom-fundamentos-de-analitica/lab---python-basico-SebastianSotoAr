"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

from datetime import datetime
from functools import reduce
from operator import itemgetter

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    sum = 0

    with open("data.csv", "r") as file:
        file = [line.split("\t") for line in file]
        file = [int(line[1]) for line in file]
        sum = reduce(lambda x, y : x + y, file)

    return sum


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    dict = {}

    with open("data.csv", "r") as file:
        file = [line.split("\t") for line in file]
        for line in file:
            key = line[0]
            dict[key] = dict.get(key, 0) + 1
    
    list = [(key, dict[key]) for key in dict]
    list = sorted(list, key = itemgetter(0))

    return list


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    dict = {}

    with open("data.csv", "r") as file:
        file = [line.split("\t") for line in file]
        for line in file:
            key = line[0]
            value = int(line[1])
            dict[key] = dict.get(key, 0) + value
    
    list = [(key, dict[key]) for key in dict]
    list = sorted(list, key = itemgetter(0))

    return list


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

    dict = {}

    with open("data.csv", "r") as file:
        file = [line.split("\t") for line in file]
        for line in file:
            key = line[2].split("-")
            key = key[1]
            value = int(line[1])
            dict[key] = dict.get(key, 0) + 1

    list = [(key, dict[key]) for key in dict]
    list = sorted(list, key = itemgetter(0))

    return list


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    dict = {}

    with open("data.csv", "r") as file:
        file = [line.split("\t") for line in file]
        for line in file:
            key = line[0]
            value = int(line[1])
            dict[key] = dict.get(key, [])
            dict[key].append(value)

        list = [(key1, max(dict[key1]), min(dict[key1])) for key1 in dict]
        list = sorted(list, key = itemgetter(0))

    return list


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    dict = {}

    with open("data.csv", "r") as file:
        file = [line.replace("\n", "") for line in file]
        file = [line.split("\t") for line in file]
        colum = [line[4].split(",") for line in file]
        list = reduce(lambda x, y: x + y, colum)
        list = [item.split(":") for item in list]
        for item in list:
            key = item[0]
            value = int(item[1])
            dict[key] = dict.get(key, [])
            dict[key].append(value)

        list1 = [(key1, min(dict[key1]), max(dict[key1])) for key1 in dict]
        list1 = sorted(list1, key = itemgetter(0))

    return list1



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    dict = {}

    with open("data.csv", "r") as file:
        file = [line.split("\t") for line in file]
        for line in file:
            key = int(line[1])
            value = line[0]
            dict[key] = dict.get(key, [])
            dict[key].append(value)

        list = [(keys, dict[keys]) for keys in dict]
        list = sorted(list, key = itemgetter(0))

    return list


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    
    dict = {}

    with open("data.csv", "r") as file:
        file = [line.split("\t") for line in file]
        for line in file:
            key = int(line[1])
            value = line[0]
            dict[key] = dict.get(key, set())
            dict[key].add(value)

        list = [(keys, dict[keys]) for keys in dict]
        list = [(keys, [value for value in values]) for keys, values in list]
        list = [(keys, sorted(lists, key = itemgetter(0))) for keys, lists in list]
        list = sorted(list, key = itemgetter(0))

    return list


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    dict = {}

    with open("data.csv", "r") as file:
        file = [line.replace("\n", "") for line in file]
        file = [line.split("\t") for line in file]
        colum = [line[4].split(",") for line in file]
        list = reduce(lambda x, y: x + y, colum)
        list = [item.split(":")[0] for item in list]
        for item in list:
            key = item
            dict[key] = dict.get(key, 0) + 1

        dict1 = {keys : dict[keys] for keys in sorted(dict)}

    return dict1


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

    list = {}

    with open("data.csv", "r") as file:
        file = [line.replace("\n", "") for line in file]
        file = [line.split("\t") for line in file]
        list = [(line[0], len(line[3].split(",")), line[4].count(":")) for line in file]

    return list


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return

if __name__ == "__main__":
    with open("data.csv", "r") as file:
        file = [line.replace("\n", "") for line in file]
        for line in file:
            print(line)

    print("\n")

    print("1\t" + str(pregunta_01()))
    print("2\t" + str(pregunta_02()))
    print("3\t" + str(pregunta_03()))
    print("4\t" + str(pregunta_04()))
    print("5\t" + str(pregunta_05()))
    print("6\t" + str(pregunta_06()))
    print("7\t" + str(pregunta_07()))
    print("8\t" + str(pregunta_08()))
    print("9\t" + str(pregunta_09()))
    print("10\t" + str(pregunta_10()))