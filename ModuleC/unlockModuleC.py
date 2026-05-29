import sys
import os
import base64
import time

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO C  |  UNLOCK
# Ejecuta este script SOLO cuando tengas los 4 fragmentos.
# ─────────────────────────────────────────────────────────
#
# [SISTEMA T.B.LODGE — autenticación de Módulo C]
#
# Estás accediendo al núcleo del servidor.
# Algo dentro del sistema ya sabe que estás aquí.
#
# ─────────────────────────────────────────────────────────

print()
print("  ┌─────────────────────────────────────────────┐")
print("  │        T.B.LODGE :: MÓDULO C — UNLOCK       │")
print("  │         Autenticación de fragmentos         │")
print("  └─────────────────────────────────────────────┘")
print()
time.sleep(1)
print("  Verificando integridad del Módulo C...")
print("  Agente registrado: T.B.LODGE (proceso interno)")
print()
time.sleep(1)

FRAGMENTOS_VALIDOS = {
    "RlJBRy1DMTo6Y29tcHJlc2lvbl9ybGU=",
    "RlJBRy1DMjo6aW50ZXJjYWxhZG8=",
    "RlJBRy1DMzo6cm90YWNpb25faXpx",
    "RlJBRy1DNDo6YXBsYW5hZG8=",
}

ingresados = set()

for i in range(1, 5):
    frag = input(f"  Fragmento C{i}: ").strip()
    frag_encoded = base64.b64encode(frag.encode()).decode()
    ingresados.add(frag_encoded)

print()

if ingresados == FRAGMENTOS_VALIDOS:
    time.sleep(0.8)
    print("  Todos los fragmentos verificados.")
    time.sleep(1)
    print()
    print("  Calculando clave del Módulo C...")
    time.sleep(1.2)
    clave = base64.b64decode("ZW50aXR5X3Vuc3RhYmxl").decode()
    print(f"  CLAVE MÓDULO C: {clave}")
    print()
    print("  Esta clave es una pieza para abrir Final.zip.")
    print("  Quedan muy pocos niveles. Algo se está estabilizando.")
    print()
else:
    faltantes = FRAGMENTOS_VALIDOS - ingresados
    print(f"  Fragmentos incorrectos o incompletos.")
    print(f"  Faltan o son inválidos: {len(faltantes)}")
    print()
    print("  Acceso denegado. El servidor no reconoce tu firma.")
    print()