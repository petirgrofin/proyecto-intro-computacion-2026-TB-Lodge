import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuleC.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO C  |  C0_MC_0
# ─────────────────────────────────────────────────────────
#
# [LOG INTERNO — T.B.LODGE — timestamp: desconocido]
#
# "Mis archivos se comprimen usando codificación
#  por longitud de racha (run-length encoding).
#  Cada secuencia de caracteres iguales consecutivos
#  se condensa en: número + carácter.
#  Así es como almaceno la memoria sin perder forma."
#  ——————————————————————
# Tu tarea: dado un string, aplicar compresión
# run-length: reemplazar grupos de caracteres repetidos
# por el número de repeticiones seguido del carácter.
# Si un carácter aparece solo una vez, solo escribe el carácter.
#
# REGLAS:
# - La función recibe un string y retorna un string
# - Grupos de 2+ iguales: escribe cantidad + carácter
# - Grupos de 1 (solos): escribe solo el carácter
# - Usa un loop para recorrer el string
# - Si el string está vacío, retorna ""
#
# Ejemplo:
#   Input:  "aaabbc"
#   Output: "3a2bc"
#
#   Input:  "aabbcc"
#   Output: "2a2b2c"
#
#   Input:  "abcd"
#   Output: "abcd"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    # TODO: Aplicar compresión run-length al string
    if len(s) == 0:
        return ""
    
    count = 1
    result = ""
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            if count == 1:
                result += s[i-1]
            else:
                result += str(count) + s[i-1]
            count = 1
    if count == 1:
        result += s[-1]
    else:
        result += str(count) + s[-1]
    return result
    pass

# ── No modifiques debajo de esta línea ──────────────────

tests = [
    ("aaabbc",      "3a2bc"),
    ("aabbcc",      "2a2b2c"),
    ("abcd",        "abcd"),
    ("",            ""),
    ("aaaa",        "4a"),
    ("aabcccdd",    "2ab3c2d"),
    ("a",           "a"),
]

_frag = "RlJBRy1DMTo6Y29tcHJlc2lvbl9ybGU="

run_tests(solution, tests, _frag,
          module="T.B.LODGE / Módulo C",
          puzzle="Puzzle 1 — Compresión de Memoria")