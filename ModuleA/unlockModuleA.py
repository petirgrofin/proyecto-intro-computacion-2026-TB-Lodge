import sys
import os
import base64
import time

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO A  |  UNLOCK
# Ejecuta este script SOLO cuando tengas los 4 fragmentos. [Y no ver sus contenidos jiji]
# ─────────────────────────────────────────────────────────
#
# [SISTEMA T.B.LODGE — autenticación de Módulo A]
#
# Los cuatro fragmentos recuperados por el detective
# deben coincidir exactamente. El servidor verifica
# cada uno antes de revelar la clave del módulo.
#
# ─────────────────────────────────────────────────────────

print()
print("  ┌─────────────────────────────────────────────┐")
print("  │        T.B.LODGE :: MÓDULO A — UNLOCK       │")
print("  │         Autenticación de fragmentos         │")
print("  └─────────────────────────────────────────────┘")
print()
time.sleep(1)
print("  Verificando integridad del Módulo A...")
print("  Agente registrado: Dr. Turing Blackmore")
print()
time.sleep(1)

FRAGMENTOS_VALIDOS = {
    "RlJBRy1BMTo6ZWNvX2ludmVyc28=",
    "RlJBRy1BMjo6dm9jZXNfbGF0ZW50ZXM=",
    "RlJBRy1BMzo6bG9kZ2VfZXNwZWpv",
    "RlJBRy1BNDo6Y2VzYXJfY2FpZG8=",
}

ingresados = set()

for i in range(1, 5):
    frag = input(f"  Fragmento A{i}: ").strip()
    frag_encoded = base64.b64encode(frag.encode()).decode()
    ingresados.add(frag_encoded)

print()

if ingresados == FRAGMENTOS_VALIDOS:
    time.sleep(0.8)
    print("  Todos los fragmentos verificados.")
    time.sleep(1)
    print()
    print("  Calculando clave del Módulo A...")
    time.sleep(1.2)
    clave = base64.b64decode("YmxhY2t3b29kX2VudHJ5").decode()
    print(f"  CLAVE MÓDULO A: {clave}")
    print()
    print("  Esta clave es una pieza para abrir Final.zip.")
    print("  Guárdala.")
    print()
else:
    faltantes = FRAGMENTOS_VALIDOS - ingresados
    print(f"  Fragmentos incorrectos o incompletos.")
    print(f"  Faltan o son inválidos: {len(faltantes)}")
    print()
    print("  Acceso denegado. El servidor no reconoce tu firma.")
    print()