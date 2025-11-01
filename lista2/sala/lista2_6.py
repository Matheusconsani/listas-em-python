import math
def resolver_equacao_2grau(a, b, c):
    if a == 0:
        return "Erro: O coeficiente 'a' não pode ser zero em uma equação de 2º grau."
    delta = b**2 - 4 * a * c
    print(f"\nDelta (Δ) = {delta}")
    if delta < 0:
        return "A equação não possui raízes reais (Delta é negativo)."
    elif delta == 0:
        x = -b / (2 * a)
        return f"A equação possui uma raiz real única: x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"A equação possui duas raízes reais:\nx1 = {x1}\nx2 = {x2}"
try:
    print("--- Calculadora de Equação de 2º Grau (ax² + bx + c = 0) ---")
    coef_a = float(input("Digite o coeficiente a: "))
    coef_b = float(input("Digite o coeficiente b: "))
    coef_c = float(input("Digite o coeficiente c: "))
    r = resolver_equacao_2grau(coef_a, coef_b, coef_c)
    print("\n")
    print(r)
except ValueError:
    print("\nERRO digite apenas números válidos para os coeficientes.")