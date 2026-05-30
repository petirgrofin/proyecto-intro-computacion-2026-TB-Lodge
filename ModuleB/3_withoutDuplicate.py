import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuleB.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO B  |  C0_MB_3
# ─────────────────────────────────────────────────────────
#
# [NOTA DE CAMPO — R. Blackwood — día 12]
#
# "Los logs se están reescribiendo. Líneas enteras
#  aparecen repetidas, como si el sistema intentara
#  reforzar ciertos mensajes. Para reconstruir el
#  registro original debo eliminar las repeticiones,
#  pero conservando el orden en que aparecieron
#  por primera vez. La secuencia importa."
#
# Tu tarea: dada una lista, retornar una nueva lista
# sin elementos duplicados, preservando el orden
# de primera aparición.
#
# REGLAS:
# - La función recibe una lista (puede tener enteros o strings)
# - Retorna una nueva lista sin duplicados
# - El orden de primera aparición debe mantenerse
# - No uses set() para resolver el problema directamente
# - Usa una lista auxiliar para llevar registro
#
# Ejemplo:
#   Input:  [1, 2, 3, 2, 1, 4]
#   Output: [1, 2, 3, 4]
#
#   Input:  ["lodge", "tb", "lodge", "blackwood", "tb"]
#   Output: ["lodge", "tb", "blackwood"]
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:


def solution(lista):
    # TODO: Retornar la lista sin duplicados, preservando orden
    nuevaLista = []  #ista vacía para guardar los elementos únicos

    for elemento in lista: # Recorre cada elemento de la lista original
        if (elemento not in nuevaLista):
            # Si es un elemento nuevo, lo añade a la lista auxiliar
            nuevaLista.append(elemento)

    return nuevaLista  # Devuelve la nueva lista sin duplicado

# ── No modifiques debajo de esta línea ──────────────────

tests = [
    ([1, 2, 3, 2, 1, 4],                        [1, 2, 3, 4]),
    (["lodge", "tb", "lodge", "blackwood", "tb"], ["lodge", "tb", "blackwood"]),
    ([5, 5, 5, 5],                               [5]),
    ([],                                          []),
    ([1, 2, 3],                                   [1, 2, 3]),
    (["a", "b", "a", "c", "b", "d"],              ["a", "b", "c", "d"]),
]

_frag = "RlJBRy1CNDo6c2luX2R1cGxpY2Fy"

run_tests(solution, tests, _frag,
          module="T.B.LODGE / Módulo B",
          puzzle="Puzzle 4 — Sin Duplicar")