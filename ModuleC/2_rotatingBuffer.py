import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuleC.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO C  |  C0_MC_2
# ─────────────────────────────────────────────────────────
#
# [LOG INTERNO — T.B.LODGE — proceso: BUFFER_ROTATE]
#
# "Mis buffers de memoria rotan continuamente.
#  Cada ciclo de proceso desplaza todos los elementos
#  N posiciones hacia la izquierda. El elemento que
#  'cae' por el borde izquierdo reaparece por la
#  derecha. Es un loop sin fin. Como yo."
# ——————————————————————
# Tu tarea: dada una tupla (lista, n), rotar la lista
# n posiciones hacia la izquierda y retornar la nueva lista.
# Rotar 1 a la izquierda significa que el primer elemento
# pasa al final.
#
# REGLAS:
# - La función recibe una tupla: (lista, n)
# - Retorna la lista rotada n posiciones a la izquierda
# - NO uses slicing con [:] para resolver el problema completo
# - Usa loops para construir la nueva lista
# - Si la lista está vacía o n es 0, retorna la misma lista
# - n puede ser mayor que el tamaño de la lista (usa módulo %)
#
# Ejemplo:
#   Input:  ([1, 2, 3, 4, 5], 2)
#   Output: [3, 4, 5, 1, 2]
#
#   Input:  ([1, 2, 3], 1)
#   Output: [2, 3, 1]
#
#   Input:  ([1, 2, 3], 3)
#   Output: [1, 2, 3]   (rotar 3 en lista de 3 = igual)
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(par):
    lista = par[0]
    n = par[1]
    # TODO: Rotar la lista n posiciones a la izquierda con loops
    # Pista: si la lista tiene largo 0, evita dividir entre 0
    if len(lista) == 0:
        return []
    n = n % len(lista)
    lista_rotada = []
    for i in range(len(lista)):
        lista_rotada.append(lista[(i+n) % len(lista)])
    return lista_rotada

    pass

# ── No modifiques debajo de esta línea ──────────────────

tests = [
    (([1, 2, 3, 4, 5], 2),      [3, 4, 5, 1, 2]),
    (([1, 2, 3], 1),            [2, 3, 1]),
    (([1, 2, 3], 3),            [1, 2, 3]),
    (([1, 2, 3, 4], 0),         [1, 2, 3, 4]),
    (([5, 6, 7, 8], 6),         [7, 8, 5, 6]),
    (([], 3),                   []),
]

_frag = "RlJBRy1DMzo6cm90YWNpb25faXpx"

run_tests(solution, tests, _frag,
          module="T.B.LODGE / Módulo C",
          puzzle="Puzzle 3 — Buffer Rotativo")