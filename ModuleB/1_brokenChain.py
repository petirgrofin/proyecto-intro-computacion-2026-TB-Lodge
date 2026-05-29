import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuleB.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO B  |  C0_MB_1
# ─────────────────────────────────────────────────────────
#
# [NOTA DE CAMPO — R. Blackwood — día 3]
#
# "Los fragmentos del log están almacenados como
#  palabras sueltas en listas. Para leer el mensaje
#  completo debo concatenarlos usando '::' como
#  separador. El sistema rechaza cualquier otro formato.
#  No puedo usar join() — el método está bloqueado
#  en este entorno restringido."
#
# Tu tarea: dada una lista de strings, retornar
# un único string donde cada elemento esté separado
# por "::" usando un loop.
# NO uses join().
#
# REGLAS:
# - La función recibe una lista de strings
# - Retorna un string con los elementos unidos por "::"
# - No se permite usar el método join()
# - Si la lista tiene un solo elemento, retórnalo tal cual
# - Si la lista está vacía, retorna string vacío ""
#
# Ejemplo:
#   Input:  ["LODGE", "SECTOR", "7", "ACTIVO"]
#   Output: "LODGE::SECTOR::7::ACTIVO"
#
#   Input:  ["blackwood"]
#   Output: "blackwood"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(lista):
    # TODO: Unir los elementos de la lista con "::" usando un loop
    resultado = ""
    contador = 0
    for elemento in lista:
        contador += 1
        resultado += elemento
        if contador < len(lista):
            resultado += "::"
        
    return resultado
    pass

# ── No modifiques debajo de esta línea ──────────────────

tests = [
    (["LODGE", "SECTOR", "7", "ACTIVO"],   "LODGE::SECTOR::7::ACTIVO"),
    (["blackwood"],                         "blackwood"),
    ([],                                    ""),
    (["a", "b", "c"],                       "a::b::c"),
    (["uno", "dos"],                        "uno::dos"),
    (["T", "B", "L", "O", "D", "G", "E"],  "T::B::L::O::D::G::E"),
]

_frag = "RlJBRy1CMjo6Y2FkZW5hX3JvdGE="

run_tests(solution, tests, _frag,
          module="T.B.LODGE / Módulo B",
          puzzle="Puzzle 2 — La Cadena Rota")