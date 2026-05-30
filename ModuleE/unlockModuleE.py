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
print("  │        T.B.LODGE :: MÓDULO E — UNLOCK       │")
print("  │         Autenticación de fragmentos         │")
print("  └─────────────────────────────────────────────┘")
print()
time.sleep(1)
print("  Verificando integridad del Módulo E...")
print("  Agente registrado: [???]")
print()
time.sleep(1.5)
print("  ...")
time.sleep(1)

FRAGMENTOS_VALIDOS = {
    "RlJBRy1FMTo6Y29ycnVwdF91bmxvY2s=",
    "RlJBRy1FMjo6d2FuZGVyaW5nX2lzX2FfdGVycmlibGVfc2lu",
    "RlJBRy1FMzo6d2hpdGVfa251Y2tsZQ==",
    "RlJBRy1FNDo6cnVu",
}

ingresados = set()

for i in range(1, 5):
    frag = input(f"  Fragmento E{i}: ").strip()
    frag_encoded = base64.b64encode(frag.encode()).decode()
    ingresados.add(frag_encoded)

print()

if ingresados == FRAGMENTOS_VALIDOS:
    time.sleep(0.8)
    print("  Todos los fragmentos verificados.")
    time.sleep(1.2)
    print()
    print("  Calculando clave del Módulo E...")
    time.sleep(1.5)
    clave = base64.b64decode("Ym9udXNfbW9kdWxlX2NvbXBsZXRlZA==").decode()
    print(f"  CLAVE MÓDULO E: {clave}")
    print()
    print("  Este es un bonus, no se ocupa para la historia.")
    print()
else:
    faltantes = FRAGMENTOS_VALIDOS - ingresados
    print(f"  Fragmentos incorrectos o incompletos.")
    print(f"  Faltan o son inválidos: {len(faltantes)}")
    print()
    print("  Acceso denegado.")
    print("  La entidad no reconoce tu firma.")
    print()