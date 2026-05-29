import sys
import os
import base64
import time

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO B  |  UNLOCK
# Ejecuta este script SOLO cuando tengas los 4 fragmentos.
# ─────────────────────────────────────────────────────────
#
# [SISTEMA T.B.LODGE — autenticación de Módulo B]
#
# El detective Blackwood accedió a este nivel
# después de semanas de trabajo. Ahora tú debes
# completar lo que él comenzó.
#
# ─────────────────────────────────────────────────────────

print()
print("  ┌─────────────────────────────────────────────┐")
print("  │        T.B.LODGE :: MÓDULO B — UNLOCK       │")
print("  │         Autenticación de fragmentos         │")
print("  └─────────────────────────────────────────────┘")
print()
time.sleep(1)
print("  Verificando integridad del Módulo B...")
print("  Agente registrado: R. Blackwood")
print()
time.sleep(1)

FRAGMENTOS_VALIDOS = {
    "RlJBRy1CMTo6dW1icmFsXzUw",
    "RlJBRy1CMjo6Y2FkZW5hX3JvdGE=",
    "RlJBRy1CMzo6cGFsYWJyYV92aXZh",
    "RlJBRy1CNDo6c2luX2R1cGxpY2Fy",
}

ingresados = set()

for i in range(1, 5):
    frag = input(f"  Fragmento B{i}: ").strip()
    frag_encoded = base64.b64encode(frag.encode()).decode()
    ingresados.add(frag_encoded)

print()

if ingresados == FRAGMENTOS_VALIDOS:
    time.sleep(0.8)
    print("  Todos los fragmentos verificados.")
    time.sleep(1)
    print()
    print("  Calculando clave del Módulo B...")
    time.sleep(1.2)
    clave = base64.b64decode("bG9kZ2VfY29ycnVwdGVk").decode()
    print(f"  CLAVE MÓDULO B: {clave}")
    print()
    print("  Esta clave es una pieza para abrir Final.zip.")
    print("  El servidor registró tu acceso. Algo lo notó.")
    print()
else:
    faltantes = FRAGMENTOS_VALIDOS - ingresados
    print(f"  Fragmentos incorrectos o incompletos.")
    print(f"  Faltan o son inválidos: {len(faltantes)}")
    print()
    print("  Acceso denegado. El servidor no reconoce tu firma.")
    print()