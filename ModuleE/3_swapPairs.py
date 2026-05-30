import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO E  |  E3
# LOGS DEL SISTEMA — Inversión de Pares de Transmisión
# ─────────────────────────────────────────────────────────
#
# Blackwood descubrió que T.B.LODGE usaba un mecanismo
# de ofuscación curioso: al transmitir datos, intercambiaba
# cada par de caracteres consecutivos entre sí.
#
# Es decir: toma los caracteres de a dos y los da vuelta.
# El carácter en posición 0 va a posición 1, y viceversa.
# Luego el de posición 2 va a posición 3, y viceversa.
# Si el string tiene longitud impar, el último carácter
# queda en su lugar.
#
# REGLAS:
# - Recibís un string
# - Intercambiá los caracteres de a pares: (0,1), (2,3), (4,5)...
# - Si el string tiene longitud impar, el último carácter no cambia
# - Retorná el string resultante
#
# Ejemplo:
#   Input:  "abcd"
#   Output: "badc"
#   (ab → ba, cd → dc)
#
#   Input:  "12345"
#   Output: "21435"
#   (12 → 21, 34 → 43, 5 → 5)
#
#   Input:  "nodo"
#   Output: "onod"
#   (no → on, do → od)
#
# ─────────────────────────────────────────────────────────
# Podés modificar el código a partir de aquí:

def solution(s):
    resultado = ""
    i = 0
    while i < len(s):
        
        if i+1 < len(s):
            # agrego al revés
            resultado += s[i+1] + s[i]
        
        else:
            # si es impar, dejo el último
            resultado += s[i]
        i += 2
    return resultado

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("abcd",      "badc"),
    ("12345",     "21435"),
    ("nodo",      "onod"),
    ("blackwood", "lbcawkood"),
    ("lodge",     "olgde"),
]

_frag = "RlJBRy1FNDo6cnVu"
run_tests(solution, tests, _frag,
          module="T.B.LODGE / Módulo E — Bonus",
          puzzle="Puzzle 4 — Inversión de Pares de Transmisión")