import base64
import time


#/─────────────────────────────────────────────────────────
# ESTE PROGRAMA ES EL JUEZ QUE VERIFICA RESPUESTAS. NO MODIFICAR.

SEPARATOR = "=" * 55

def run_tests(solution_func, tests, encoded_password, module=None, puzzle=None):
    print(SEPARATOR)
    if module:
        print(f"  Caso :: {module}")
    if puzzle:
        print(f"  {puzzle}")
    print(SEPARATOR)
    print()

    passed = 0
    for i, (inp, expected) in enumerate(tests):
        try:
            result = solution_func(inp)
        except Exception as e:
            print(f"  [FAIL] Test {i+1} — excepción: {e}")
            print()
            print("  Sistema no puede continuar.")
            print(SEPARATOR)
            return

        if result != expected:
            print(f"  [FAIL] Test {i+1}")
            print(f"    Input    : {repr(inp)}")
            print(f"    Esperado : {repr(expected)}")
            print(f"    Obtenido : {repr(result)}")
            print()
            print("  Acceso denegado. Intenta de nuevo.")
            print(SEPARATOR)
            return
        else:
            print(f"  [OK] Test {i+1} — correcto")
            passed += 1

    print()
    print(f"  {passed}/{len(tests)} tests superados.")
    print()
    time.sleep(0.6)
    print("  Desencriptando fragmento...")
    time.sleep(0.8)
    password = base64.b64decode(encoded_password).decode()
    print(f"  FRAGMENTO DESBLOQUEADO: {password}")
    print()
    print(SEPARATOR)
