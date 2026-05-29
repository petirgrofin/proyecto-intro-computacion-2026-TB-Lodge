import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuleC.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO C  |  C0_MC_4
# ─────────────────────────────────────────────────────────
#
# [LOG INTERNO — T.B.LODGE — proceso: MEMORY_FLATTEN]
#
# "Mi memoria está fragmentada en bloques anidados.
#  Para reconstruir el estado completo necesito
#  aplanar todas las capas en una sola secuencia
#  lineal. Los bloques dentro de bloques deben
#  desplegarse. Solo hay un nivel de anidamiento."
#
# Tu tarea: dada una lista de listas, retornar
# una sola lista con todos los elementos en orden,
# sin sublistas. Solo hay un nivel de anidamiento
# (listas dentro de una lista, no listas dentro
# de listas dentro de listas).
#
# REGLAS:
# - La función recibe una lista de listas
# - Retorna una lista plana con todos los elementos
# - Mantén el orden: primero todos los de la primera sublista,
#   luego los de la segunda, etc.
# - Usa loops anidados (for dentro de for)
# - Si la lista está vacía, retorna []
# - Las sublistas también pueden estar vacías
#
# Ejemplo:
#   Input:  [[1, 2], [3, 4], [5]]
#   Output: [1, 2, 3, 4, 5]
#
#   Input:  [[10, 20], [], [30]]
#   Output: [10, 20, 30]
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(lista_de_listas):
    # TODO: Aplanar la lista de listas usando loops anidados
    if len(lista_de_listas) == 0:
        return []
    lista_plana = []
    for sublista in lista_de_listas:
        for elemento in sublista:
            lista_plana.append(elemento)
    return lista_plana

# ── No modifiques debajo de esta línea ──────────────────

tests = [
    ([[1, 2], [3, 4], [5]],              [1, 2, 3, 4, 5]),
    ([[10, 20], [], [30]],               [10, 20, 30]),
    ([[], [], []],                        []),
    ([],                                  []),
    ([["a", "b"], ["c"]],                ["a", "b", "c"]),
    ([[1], [2], [3], [4]],               [1, 2, 3, 4]),
]

_frag = "RlJBRy1DNDo6YXBsYW5hZG8="

run_tests(solution, tests, _frag,
          module="T.B.LODGE / Módulo C",
          puzzle="Puzzle 4 — Memoria Aplanada")