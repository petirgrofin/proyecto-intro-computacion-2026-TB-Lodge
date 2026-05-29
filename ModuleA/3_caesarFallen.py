import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuleA.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO A  |  PUZZLE 4
# AGENTE: Dr. Turing Blackmore (el Investigador)
# ─────────────────────────────────────────────────────────
#
# [BITÁCORA — entrada 004 — Dr. Blackmore]
#
# "El último log del profesor está cifrado con un
#  método que él llamaba 'el turno de César'.
#  Cada letra fue desplazada 3 posiciones hacia adelante
#  en el alfabeto. Para leerlo, debo revertir ese
#  desplazamiento: mover cada letra 3 posiciones atrás.
#  Los caracteres que no son letras no cambian."
#
# Tu tarea: descifrar un string cifrado con César
# de desplazamiento 3. Mueve cada letra 3 posiciones
# hacia atrás en el alfabeto. No-letras quedan igual.
#
# El alfabeto es solo letras minúsculas (a-z).
# Pista: el código ASCII de 'a' es 97.
#        ord('a') = 97,  chr(97) = 'a'
#
# REGLAS:
# - La función recibe un string (solo minúsculas y espacios)
# - Retorna el string descifrado
# - Solo descifras letras minúsculas (a-z)
# - Espacios y otros caracteres quedan igual
# - El desplazamiento es SIEMPRE 3 (hacia atrás)
# - El alfabeto es circular: 'a' - 3 = 'x'
#
# Ejemplo:
#   Input:  "orgjh"       (cifrado)
#   Output: "lodge"       (descifrado)
#
#   Input:  "eodfnzrrg"
#   Output: "blackwood"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    decoded_string = ""
    for char in s:
        if ('a' <= char <= 'z'): # solo se descifran letras minúscula
            char_code = ord(char)
            decoded_char_ord = char_code - 3 # se desplazan tres hacia atrás
            if decoded_char_ord < ord('a'):
                decoded_char_ord += 26 # se suman las 26 letras del alfabeto para hacerlo circular
            decoded_string += chr(decoded_char_ord)
        else:
            decoded_string += char
    return decoded_string


# ── No modifiques debajo de esta línea ──────────────────

tests = [
    ("orgjh",             "lodge"),
    ("eodfnzrrg",         "blackwood"),
    ("defa",              "abcx"),
    ("khoor zruog",       "hello world"),
    ("wkh vhuyhu olyhv",  "the server lives"),
    ("abc",               "xyz"),
]

_frag = "RlJBRy1BNDo6Y2VzYXJfY2FpZG8="

run_tests(solution, tests, _frag,
          module="T.B.LODGE / Módulo A",
          puzzle="Puzzle 4 — El Turno de César")
