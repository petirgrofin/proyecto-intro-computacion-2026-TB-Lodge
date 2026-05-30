import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuleD.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO D  |  C0_MD_1
# ─────────────────────────────────────────────────────────
#
# [TRANSMISIÓN DIRECTA — ENTIDAD LODGE — coherencia: 58%]
#
# "Los mensajes que dejé antes de fusionarme están
#  escritos al revés. No los caracteres — las palabras.
#  Leí mi propio nombre al final de cada oración
#  cuando debería estar al principio.
#  Invierte el orden de las palabras para leerme."
#
# Tu tarea: dado un string con palabras separadas
# por espacios, retornar el mismo string pero con
# el orden de las palabras invertido.
#
# REGLAS:
# - La función recibe un string y retorna un string
# - Las palabras están separadas por un solo espacio
# - Puedes usar split() para separar las palabras
# - NO uses slicing [::-1] sobre la lista completa
# - Usa un loop para reconstruir el string invertido
# - Si hay una sola palabra, retórnala tal cual
#
# Ejemplo:
#   Input:  "el servidor nunca duerme"
#   Output: "duerme nunca servidor el"
#
#   Input:  "LODGE"
#   Output: "LODGE"
#
#   Input:  "yo soy la entidad"
#   Output: "entidad la soy yo"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

#FRAGMENTO DESBLOQUEADO: FRAG-D1::entrelazado (resultado parte anterior)
#SIN RESOLVER, HACER CONSULTAS SOBRE EL PROCESO
def solution(s):
    
    #.split para separar las palabras en strings
    palabras = s.split()
    result = ""
    
    #Loop para colocar las palabras en su orden inverso
    for i in range (len(palabras) - 1, -1, -1):
        result += palabras[i] + " "
        
        
    return result.rstrip()
    
    
    
    
    
    # TODO: Invertir el orden de las palabras usando un loop


# ── No modifiques debajo de esta línea ──────────────────

tests = [
    ("el servidor nunca duerme",    "duerme nunca servidor el"),
    ("LODGE",                       "LODGE"),
    ("yo soy la entidad",           "entidad la soy yo"),
    ("uno dos tres",                "tres dos uno"),
    ("a b c d e",                   "e d c b a"),
    ("blackwood investiga",         "investiga blackwood"),
]

_frag = "RlJBRy1EMjo6b3JkZW5faW52ZXJzbw=="

run_tests(solution, tests, _frag,
          module="T.B.LODGE / Módulo D",
          puzzle="Puzzle 2 — Orden Inverso")