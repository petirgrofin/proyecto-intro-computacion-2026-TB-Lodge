import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuleA.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO A  |  PUZZLE C0_MA_0
# ─────────────────────────────────────────────────────────
#
# [BITÁCORA — entrada 001 — Dr. Blackmore]
#
# "El servidor almacena los mensajes al revés.
#  No sé si es un protocolo de seguridad o un síntoma
#  de algo peor. Para leer cualquier log, primero
#  debo invertir cada línea carácter por carácter."
#  ——————————————————————
# Tu tarea: dado un string, devolver ese mismo string
# pero con los caracteres en orden inverso.
# NO uses slicing (s[::-1]). Usa un loop.
#
# REGLAS:
# - La función recibe un string y retorna un string
# - Debes recorrer el string con un for o while
# - No se permite usar s[::-1] ni reversed()
# - Si el string está vacío, retorna string vacío
#
# Ejemplo:
#   Input:  "LODGE"
#   Output: "EGDOL"
#
#   Input:  "hola mundo"
#   Output: "odnum aloh"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    result = ""
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result

# ── No modifiques debajo de esta línea ──────────────────

tests = [
    ("LODGE",        "EGDOL"),
    ("hola mundo",   "odnum aloh"),
    ("abcde",        "edcba"),
    ("racecar",      "racecar"),
    ("",             ""),
    ("x",            "x"),
]

_frag = "RlJBRy1BMTo6ZWNvX2ludmVyc28="
run_tests(solution, tests, _frag,
          module="T.B.LODGE / Módulo A",
          puzzle="Puzzle 1 — El Eco Invertido")
