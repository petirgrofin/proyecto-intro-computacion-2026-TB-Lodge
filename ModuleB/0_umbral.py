import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuleB.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO B  |  C0_MB_0
# ─────────────────────────────────────────────────────────
#
# [NOTA DE CAMPO — R. Blackwood — día 1]
#
# "El servidor registra temperaturas del procesador
#  cada segundo. Valores por encima de 50 indican
#  actividad anormal: el sistema se está ejecutando
#  algo que no debería. Necesito aislar esas lecturas
#  para saber cuándo ocurre el fenómeno."
# —————————————————————
# Tu tarea: dada una lista de números enteros,
# retornar una nueva lista con solo los elementos
# mayores a 50 (estrictamente mayor, no igual).
#
# REGLAS:
# - La función recibe una lista de enteros
# - Retorna una nueva lista (no modifica la original)
# - Solo incluye elementos donde el valor > 50
# - Mantén el orden original
# - Si ninguno cumple, retorna lista vacía []
#
# Ejemplo:
#   Input:  [30, 55, 12, 78, 50, 91]
#   Output: [55, 78, 91]
#
#   Input:  [10, 20, 30]
#   Output: []
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(lista):
    # TODO: Filtrar la lista y retornar solo los elementos > 50
    resultado = []
    for item in lista:
        if (item > 50):
            resultado.append(item)
    return resultado


solution([30, 55, 12, 78, 50, 91])

# ── No modifiques debajo de esta línea ──────────────────

tests = [
    ([30, 55, 12, 78, 50, 91],     [55, 78, 91]),
    ([10, 20, 30],                  []),
    ([51, 52, 53],                  [51, 52, 53]),
    ([50, 50, 50],                  []),
    ([],                            []),
    ([100, 1, 99, 2, 75],           [100, 99, 75]),
]

_frag = "RlJBRy1CMTo6dW1icmFsXzUw"

run_tests(solution, tests, _frag,
          module="T.B.LODGE / Módulo B",
          puzzle="Puzzle 1 — El Umbral Térmico")