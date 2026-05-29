import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuleA.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO A  |  PUZZLE C0_MA_2
# ─────────────────────────────────────────────────────────
#
# [BITÁCORA — entrada 003 — Dr. Blackmore]
#
# "Los archivos del profesor tienen una firma oculta.
#  Sus mensajes más importantes son palíndromos:
#  se leen igual de izquierda a derecha que al revés.
#  El sistema los usa como claves de autenticación.
#  Necesito un detector para identificarlos."
#  —————————————————————
# Tu tarea: dado un string, retornar True si es un
# palíndromo, o False si no lo es.
# Compara letra por letra usando un loop.
#
# REGLAS:
# - La función recibe un string y retorna True o False
# - El string ya viene en minúsculas y sin espacios
# - Usa un loop para comparar; no uses s[::-1]
# - Un string vacío o de 1 carácter es palíndromo
#
# Ejemplo:
#   Input:  "radar"
#   Output: True
#
#   Input:  "lodge"
#   Output: False
#
#   Input:  "anitalavalatina"
#   Output: True
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    reversed_string = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_string += s[i]
    return s == reversed_string

# Alternativamente, con la técnica de two pointers:
def alt_solution(s):
    i = 0
    j = len(s) - 1
    is_palindrome = True
    while i < j and is_palindrome:
        is_palindrome = s[i] == s[j]
        i += 1
        j -= 1
    return is_palindrome

 
# ── No modifiques debajo de esta línea ──────────────────

tests = [
    ("radar",              True),
    ("lodge",              False),
    ("anitalavalatina",    True),
    ("racecar",            True),
    ("blackmore",          False),
    ("",                   True),
    ("a",                  True),
    ("abcba",              True),
]

_frag = "RlJBRy1BMzo6bG9kZ2VfZXNwZWpv"

run_tests(solution, tests, _frag,
          module="T.B.LODGE / Módulo A",
          puzzle="Puzzle 3 — El Espejo del Lodge")
