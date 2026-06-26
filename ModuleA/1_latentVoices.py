import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuleA.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO A  |  PUZZLE C0_MA_1
# ─────────────────────────────────────────────────────────
#
# [BITÁCORA — entrada 002 — Dr. Blackmore]
#
# "Encontré un patrón en los logs del servidor.
#  Los archivos corruptos tienen exactamente el doble
#  de vocales que los archivos limpios. Para filtrar
#  el ruido, necesito un contador de vocales preciso.
#  Mayúsculas y minúsculas cuentan igual."
# ——————————————————————
# Tu tarea: dado un string, retornar cuántas vocales
# contiene. Las vocales son: a, e, i, o, u
# (mayúsculas y minúsculas cuentan).
#
# REGLAS:
# - La función recibe un string y retorna un entero
# - Vocales válidas: a, e, i, o, u (y sus mayúsculas)
# - Usa un loop para recorrer el string
# - No se permite usar count() directamente
#
# Ejemplo:
#   Input:  "T.B.LODGE"
#   Output: 2
#
#   Input:  "Blackmore"
#   Output: 4
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

# Se crea un arreglo con las vocales en minúscula. Posteriormente, se itera sobre cada carácter 
# en la cadena dada usando char.lower() para pasarlas a minúscula y el keyword reservado "in" para
# determinar cuántos caracteres son vocales. Cada uno se suma a la variable total.
def solution(s):
    vocals = ["a", "e", "i", "o", "u"]
    total = 0
    for char in s:
        if char.lower() in vocals:
            total += 1 
    return total
    

# ── No modifiques debajo de esta línea ──────────────────

tests = [
    ("T.B.LODGE",       2),
    ("Blackmore",       3),
    ("aeiouAEIOU",      10),
    ("rythmn",          0),
    ("",                0),
    ("El servidor vive", 6),
]

_frag ="RlJBRy1BMjo6dm9jZXNfbGF0ZW50ZXM="

run_tests(solution, tests, _frag,
          module="T.B.LODGE / Módulo A",
          puzzle="Puzzle 2 — Voces Latentes")
