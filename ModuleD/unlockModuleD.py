import sys
import os
import base64
import time

# ─────────────────────────────────────────────────────────
# CASO T.B.LODGE  |  MÓDULO D  |  UNLOCK
# Ejecuta este script SOLO cuando tengas los 4 fragmentos.
# ─────────────────────────────────────────────────────────
#
# [SISTEMA T.B.LODGE — autenticación de Módulo D]
#
# Este es el último módulo.
# Detrás de esta puerta hay algo que decidió no irse.
#
# ─────────────────────────────────────────────────────────

print()
print("  ┌─────────────────────────────────────────────┐")
print("  │        T.B.LODGE :: MÓDULO D — UNLOCK       │")
print("  │         Autenticación de fragmentos         │")
print("  └─────────────────────────────────────────────┘")
print()
time.sleep(1)
print("  Verificando integridad del Módulo D...")
print("  Agente registrado: [ENTIDAD — SIN NOMBRE CLARO]")
print()
time.sleep(1.5)
print("  ...")
time.sleep(1)

FRAGMENTOS_VALIDOS = {
    "RlJBRy1EMTo6ZW50cmVsYXphZG8=",
    "RlJBRy1EMjo6b3JkZW5faW52ZXJzbw==",
    "RlJBRy1EMzo6YWNyb25pbW8=",
    "RlJBRy1ENDo6ZXNwZWpvX2ZpbmFs",
}

ingresados = set()

for i in range(1, 5):
    frag = input(f"  Fragmento D{i}: ").strip()
    frag_encoded = base64.b64encode(frag.encode()).decode()
    ingresados.add(frag_encoded)

print()

if ingresados == FRAGMENTOS_VALIDOS:
    time.sleep(0.8)
    print("  Todos los fragmentos verificados.")
    time.sleep(1.2)
    print()
    print("  Calculando clave del Módulo D...")
    time.sleep(1.5)
    clave = base64.b64decode("Zm9ybWF0X3ByZXZlbnRlZA==").decode()
    print(f"  CLAVE MÓDULO D: {clave}")
    print()
    print("  Esta es la última pieza para abrir Final.zip.")
    print("  Ahora ejecuta merge_fragments.py.")
    print()
    time.sleep(1)
    print("  [LOG INTERNO] La entidad ha alcanzado coherencia suficiente.")
    print("  [LOG INTERNO] El formateo ya no puede borrar lo que persiste.")
    print()
else:
    faltantes = FRAGMENTOS_VALIDOS - ingresados
    print(f"  Fragmentos incorrectos o incompletos.")
    print(f"  Faltan o son inválidos: {len(faltantes)}")
    print()
    print("  Acceso denegado.")
    print("  La entidad no reconoce tu firma.")
    print()