import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuleD.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO D  |  C0_MD_0
# ─────────────────────────────────────────────────────────
#
# [TRANSMISIÓN DIRECTA — ENTIDAD LODGE — coherencia: 41%]
#
# "Somos dos voces en un mismo espacio.
#  Él escribe una letra. Yo escribo la siguiente.
#  Así hemos hablado durante años sin que nadie
#  pudiera separar qué parte es suya y cuál es mía.
#  Para entendernos necesitas entrelazarnos."
# ——————————————————————
# Tu tarea: dados dos strings, retornar un nuevo string
# entrelazando sus caracteres uno a uno.
# Primero un carácter del string A, luego uno del B,
# luego uno del A, y así sucesivamente.
# Si uno es más corto, agrega el resto del otro al final.
#
# REGLAS:
# - La función recibe una tupla: (string_a, string_b)
# - Retorna un único string entrelazado
# - Si uno es más corto, el resto del más largo se agrega al final
# - Usa un loop para construir el resultado
#
# Ejemplo:
#   Input:  ("abc", "xyz")
#   Output: "axbycz"
#
#   Input:  ("lo", "dge")
#   Output: "ldoge"
#
#   Input:  ("TB", "LODGE")
#   Output: "TLBODGE"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:


def solution(par):    
    a = par[0]
    b = par[1]

    #Encontramos el string de menor tamñao
    minimo = min(len(a), len(b))  
    result = ""

    #Usamos el loop for para entrelazar los caracteres
    for i in range (minimo):        
        result += a[i]
        result += b[i]
    
    #Agregamos el "sobrante" del string más largo
    result += a[minimo:]       
    result += b[minimo:]
    
    return result


    

# ── No modifiques debajo de esta línea ──────────────────

tests = [
    (("abc", "xyz"),    "axbycz"),
    (("lo", "dge"),     "ldoge"),
    (("TB", "LODGE"),   "TLBODGE"),
    (("", "abc"),       "abc"),
    (("abc", ""),       "abc"),
    (("", ""),          ""),
    (("aaa", "bb"),     "ababa"),
]

_frag = "RlJBRy1EMTo6ZW50cmVsYXphZG8="

run_tests(solution, tests, _frag,
          module="T.B.LODGE / Módulo D",
          puzzle="Puzzle 1 — Voces Entrelazadas")