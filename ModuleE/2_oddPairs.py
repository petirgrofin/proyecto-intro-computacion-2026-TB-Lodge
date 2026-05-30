import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from judge import run_tests
import base64

# ---------------------------------------------------------
# CASO T.B.LODGE  |  MODULO E  |  E2
# NIVEL PROFUNDO -- Selector de Cadenas Impares
# ---------------------------------------------------------
#
# El nucleo de T.B.LODGE filtra identificadores de memoria
# usando un criterio poco usual: solo acepta palabras cuya
# longitud sea un numero IMPAR (1, 3, 5, 7...).
#
# Las palabras de longitud par son descartadas como
# "estructuras inestables" dentro del sistema.
#
# REGLAS:
# - Recibis una lista de strings
# - Devuelve una nueva lista con SOLO las palabras cuya
#   longitud sea impar (len % 2 != 0)
# - Conserva el orden original
# - Si no hay ninguna, retorna lista vacia []
#
# Ejemplo:
#   Input:  ["lodge", "nodo", "eco", "servidor"]
#   Output: ["lodge", "eco"]
#   (lodge=5 impar, nodo=4 par, eco=3 impar, servidor=8 par)
#
#   Input:  ["a", "bb", "ccc", "dddd"]
#   Output: ["a", "ccc"]
#
#   Input:  ["ab", "cd", "ef"]
#   Output: []
#
# ---------------------------------------------------------
# Podes modificar el codigo a partir de aqui:

def solution(lista):
    nueva_lista = []
    for palabra in lista:
        if len(palabra) % 2 != 0:
            nueva_lista.append(palabra)
    return nueva_lista

# -- No modifiques debajo de esta linea ------------------
tests = [
    (["lodge", "nodo", "eco", "servidor"],          ["lodge", "eco"]),
    (["blackwood", "log", "ok"],                    ["blackwood", "log"]),
    (["a", "bb", "ccc", "dddd"],                    ["a", "ccc"]),
    (["sistema", "activo", "error"],                ["sistema", "error"]),
    (["ab", "cd", "ef"],                            []),
]

_frag = "RlJBRy1FMzo6d2hpdGVfa251Y2tsZQ=="
run_tests(solution, tests, _frag,
          module="T.B.LODGE / Modulo E -- Bonus",
          puzzle="Puzzle 2 -- Selector de Cadenas Impares")