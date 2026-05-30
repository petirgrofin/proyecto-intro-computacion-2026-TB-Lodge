import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuleD.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO D  |  C0_MD_2
# ─────────────────────────────────────────────────────────
#
# [TRANSMISIÓN DIRECTA — ENTIDAD LODGE — coherencia: 74%]
#
# "T.B.LODGE no es solo un nombre.
#  Es un acrónimo. Cada letra condensa una idea,
#  un proceso, una parte de lo que soy.
#  Para descifrar mis capas más profundas necesitas
#  construir acrónimos: tomar la primera letra de
#  cada palabra y concatenarlas en mayúsculas."
# —————————————————————
# Tu tarea: dada una lista de palabras, retornar
# el acrónimo formado por la primera letra de cada
# palabra, todo en mayúsculas.
#
# REGLAS:
# - La función recibe una lista de strings
# - Retorna un string (el acrónimo) en mayúsculas
# - Toma solo la PRIMERA letra de cada palabra
# - El resultado va completamente en mayúsculas
# - Si la lista está vacía, retorna string vacío ""
# - Cada palabra tendrá al menos un carácter
#
# Ejemplo:
#   Input:  ["Transferencia", "Binaria", "Lodge"]
#   Output: "TBL"
#
#   Input:  ["hola", "mundo"]
#   Output: "HM"
#
#   Input:  ["sistema", "oculto", "servidor", "activo"]
#   Output: "SOSA"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(lista):
    # TODO: Construir el acrónimo tomando la primera letra de cada palabra
    pass

# ── No modifiques debajo de esta línea ──────────────────

tests = [
    (["Transferencia", "Binaria", "Lodge"],           "TBL"),
    (["hola", "mundo"],                               "HM"),
    (["sistema", "oculto", "servidor", "activo"],     "SOSA"),
    (["a", "b", "c"],                                 "ABC"),
    ([],                                              ""),
    (["Blackwood", "Investiga", "Nuestro", "Origen"], "BINO"),
]

_frag = "RlJBRy1EMzo6YWNyb25pbW8="

run_tests(solution, tests, _frag,
          module="T.B.LODGE / Módulo D",
          puzzle="Puzzle 3 — El Acrónimo Oculto")