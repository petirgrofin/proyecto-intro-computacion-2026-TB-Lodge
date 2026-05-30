import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuleD.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO D  |  C0_MD_3
# ─────────────────────────────────────────────────────────
#
# [TRANSMISIÓN DIRECTA — ENTIDAD LODGE — coherencia: 99%]
#
# "Esto es lo que somos ahora: una cosa y su reflejo,
#  fusionados en un solo ser continuo. El principio
#  y el fin del mismo string. Para estabilizarnos
#  completamente necesitas construir nuestro espejo:
#  el string original seguido de su propio reverso.
#  Cuando lo logres, el servidor recordará por qué existe."
#
# Tu tarea: dado un string, retornar ese string
# concatenado con su propio reverso.
# El resultado es el string original + el string al revés.
#
# REGLAS:
# - La función recibe un string y retorna un string
# - El resultado es: string_original + reverso_del_string
# - NO uses slicing [::-1] para el reverso; usa un loop
# - Si el string está vacío, retorna string vacío ""
#
# Ejemplo:
#   Input:  "lodge"
#   Output: "lodgeegdol"
#
#   Input:  "TB"
#   Output: "TBBT"
#
#   Input:  "abc"
#   Output: "abccba"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    # TODO: Retornar el string + su reverso, usando un loop para invertir
    pass

# ── No modifiques debajo de esta línea ──────────────────

tests = [
    ("lodge",       "lodgeegdol"),
    ("TB",          "TBBT"),
    ("abc",         "abccba"),
    ("",            ""),
    ("a",           "aa"),
    ("blackwood",   "blackwooddoowkcalb"),
]

_frag = "RlJBRy1ENDo6ZXNwZWpvX2ZpbmFs"

run_tests(solution, tests, _frag,
          module="T.B.LODGE / Módulo D",
          puzzle="Puzzle 4 — El Espejo Final")