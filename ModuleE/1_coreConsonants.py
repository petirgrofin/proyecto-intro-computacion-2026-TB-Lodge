import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from judge import run_tests
import base64

# ---------------------------------------------------------
# CASO T.B.LODGE  |  MODULO E  |  E1
# NIVEL PROFUNDO -- Conteo de Consonantes en el Nucleo
# ---------------------------------------------------------
#
# Has llegado al nivel mas profundo de T.B.LODGE.
# El sistema aqui mide la "densidad de consonantes"
# en los identificadores internos: cuantas letras
# NO son vocales tiene cada cadena de texto.
#
# Necesitas contar cuantas consonantes hay en un string.
# Las vocales son: a, e, i, o, u (en minusculas y mayusculas).
# Solo cuentan letras del alfabeto; los espacios, numeros
# y simbolos se ignoran completamente.
#
# REGLAS:
# - Recibis un string con letras, espacios u otros caracteres
# - Conta cuantos caracteres son letras del alfabeto Y NO son vocales
# - Las mayusculas y minusculas de las consonantes cuentan igual
# - Retorna un entero
#
# Ejemplo:
#   Input:  "blackwood"
#   Output: 6
#   (b, l, c, k, w, d son consonantes; a, o, o son vocales)
#
#   Input:  "aeiou"
#   Output: 0
#   (solo vocales, ninguna consonante)
#
#   Input:  "lodge"
#   Output: 3
#   (l, d, g son consonantes; o, e son vocales)
#
# ---------------------------------------------------------
# Podes modificar el codigo a partir de aqui:

def solution(s):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in s:
        # si es letra Y no es vocal
        
        if caracter.isalpha() and caracter not in vocales:
            contador += 1
    return contador

# -- No modifiques debajo de esta linea ------------------
tests = [
    ("blackwood", 6),
    ("aeiou",     0),
    ("lodge",     3),
    ("servidor",  5),
    ("tblodge",   5),
]

_frag = "RlJBRy1FMjo6d2FuZGVyaW5nX2lzX2FfdGVycmlibGVfc2lu"
run_tests(solution, tests, _frag,
          module="T.B.LODGE / Modulo E -- Bonus",
          puzzle="Puzzle 2 -- Conteo de Consonantes en el Nucleo")