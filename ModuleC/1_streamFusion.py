import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuleC.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO C  |  C0_MC_1
# ─────────────────────────────────────────────────────────
#
# [LOG INTERNO — T.B.LODGE — proceso: MERGE_STREAM]
#
# "Mis dos flujos de datos —el del profesor y el del
#  detective— deben fusionarse en un solo stream.
#  El protocolo es estricto: un elemento de cada lista
#  en alternancia. Primero uno de A, luego uno de B,
#  luego uno de A, luego uno de B...
#  Si una lista es más corta, los elementos restantes
#  de la otra se agregan al final."
# ——————————————————————
# Tu tarea: dadas dos listas, retornar una nueva lista
# intercalando sus elementos uno a uno.
# Los elementos sobrantes se agregan al final.
#
# REGLAS:
# - La función recibe una tupla: (lista_a, lista_b)
# - Retorna una sola lista intercalada
# - Si las listas tienen distinto tamaño, agrega el resto al final
# - Si ambas están vacías, retorna []
#
# Ejemplo:
#   Input:  ([1, 2, 3], [4, 5, 6])
#   Output: [1, 4, 2, 5, 3, 6]
#
#   Input:  ([1, 2], [3, 4, 5, 6])
#   Output: [1, 3, 2, 4, 5, 6]
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(par):
    
    lista_a = par[0]
    lista_b = par[1]
    lista_c = []
    for a, b in zip(lista_a, lista_b):
        lista_c.append(a)
        lista_c.append(b)
    contador = min(len(lista_a), len(lista_b))
    restante = lista_a[contador:] + lista_b[contador:]
    return(lista_c + restante)
      
    # TODO: Intercalar los elementos de lista_a y lista_b
    pass

# ── No modifiques debajo de esta línea ──────────────────

tests = [
    (([1, 2, 3], [4, 5, 6]),             [1, 4, 2, 5, 3, 6]),
    (([1, 2], [3, 4, 5, 6]),             [1, 3, 2, 4, 5, 6]),
    (([1, 2, 3, 4], [5, 6]),             [1, 5, 2, 6, 3, 4]),
    (([], [1, 2, 3]),                    [1, 2, 3]),
    (([1, 2, 3], []),                    [1, 2, 3]),
    ((["a", "b"], ["x", "y"]),           ["a", "x", "b", "y"]),
]

_frag = "RlJBRy1DMjo6aW50ZXJjYWxhZG8="

run_tests(solution, tests, _frag,
          module="T.B.LODGE / Módulo C",
          puzzle="Puzzle 2 — Fusión de Streams")