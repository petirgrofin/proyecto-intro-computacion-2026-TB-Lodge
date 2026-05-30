import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO E  |  E0
# LOGS DEL SISTEMA — Expansión de Señal Comprimida
# ─────────────────────────────────────────────────────────
#
# El servidor T.B.LODGE almacenaba datos en un formato
# comprimido: en lugar de repetir un carácter varias veces,
# guardaba el carácter seguido del número de repeticiones.
#
# Por ejemplo: en vez de guardar "aaabbc", guardaba "a3b2c1".
#
# Los logs más recientes llegaron en este formato comprimido.
# Para leerlos, necesitás EXPANDIRLOS: reconstruir el string
# original a partir del formato comprimido.
#
# REGLAS:
# - Recibís un string en formato: carácter + dígito, alternando
# - Cada par (carácter, dígito) indica: repetir ese carácter
#   esa cantidad de veces
# - El string siempre tiene longitud par
# - El dígito siempre es un número del 1 al 9
# - Retorná el string expandido
#
# Ejemplo:
#   Input:  "a3b2c1"
#   Output: "aaabbc"
#
#   Input:  "x4y1"
#   Output: "xxxxy"
#
#   Input:  "n2o1d2"
#   Output: "nnodd"
#
# ─────────────────────────────────────────────────────────
# Podés modificar el código a partir de aquí:

def solution(s):
    resultado = ""
    
    # ciclo de a 2 en 2：0, 2, 4...
    for i in range(0, len(s), 2):
        letra = s[i]
        # agarro la letra
        
        numero = int(s[i+1])
        # agarro el número
        
        resultado += letra * numero
        # repito la letra
        
    return resultado

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("a3b2c1",  "aaabbc"),
    ("x4y1",    "xxxxy"),
    ("l1o3p2",  "looopp"),
    ("n2o1d2",  "nnodd"),
    ("t1b1l2",  "tbll"),
]


_frag = "RlJBRy1FMTo6Y29ycnVwdF91bmxvY2s="

run_tests(solution, tests, _frag,
          module="T.B.LODGE / Módulo E — Bonus",
          puzzle="Puzzle 0 — Expansión de Señal Comprimida")