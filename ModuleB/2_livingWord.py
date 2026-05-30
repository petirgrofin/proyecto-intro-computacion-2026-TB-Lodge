import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuleB.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO B  |  C0_MB_2
# ─────────────────────────────────────────────────────────
#
# [NOTA DE CAMPO — R. Blackwood — día 7]
#
# "El sistema tiene una convención extraña: dentro de
#  cada línea de log, la palabra más larga es siempre
#  la clave de ese registro. Es como si el profesor
#  hubiera escondido información a plena vista,
#  sabiendo que nadie leería con cuidado."
#
# Tu tarea: dado un string con palabras separadas
# por espacios, retornar la palabra más larga.
# Si hay empate, retorna la primera que aparece.
#
# REGLAS:
# - La función recibe un string
# - Retorna la palabra más larga (string)
# - Si hay empate en longitud, retorna la primera
# - Puedes usar split() para separar las palabras
# - Usa un loop para encontrar la más larga
# - No uses max() con key=
#
# Ejemplo:
#   Input:  "el servidor nunca duerme"
#   Output: "servidor"
#
#   Input:  "lodge tb"
#   Output: "lodge"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    # TODO: Encontrar y retornar la palabra más larga del string
    resultado = ""  # Guarda la palabra más larga encontrada
    texto = s.split()
    for palabra in texto: # Recorre cada palabra de la lista una por una
        if len(palabra) > len(resultado):
            resultado = palabra # Reemplaza la palabra guardada por la nueva más larga

    return resultado  # Devuelve la palabra más larga

# ── No modifiques debajo de esta línea ──────────────────

tests = [
    ("el servidor nunca duerme",            "servidor"),
    ("lodge tb",                            "lodge"),
    ("blackwood investiga el caso",         "blackwood"),
    ("a bb ccc dd e",                       "ccc"),
    ("uno",                                 "uno"),
    ("iguales letras",                      "iguales"),
]

_frag = "RlJBRy1CMzo6cGFsYWJyYV92aXZh"

run_tests(solution, tests, _frag,
          module="T.B.LODGE / Módulo B",
          puzzle="Puzzle 3 — La Palabra Viva")