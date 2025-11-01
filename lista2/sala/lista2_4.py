try:
    l1 = float(input("Digite o valor do lado A: "))
    l2 = float(input("Digite o valor do lado B: "))
    l3 = float(input("Digite o valor do lado C: "))
except ValueError:
    print("ERRO: Por favor, digite apenas números válidos.")
    exit()
if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    if l1 == l2 and l2 == l3:
        res = "O triângulo é **EQUILÁTERO**."
    elif l1 == l2 or l2 == l3 or l1 == l3:
        res = "O triângulo é **ISÓSCELES**."
    else:
        res = "O triângulo é **ESCALENO**."
    print("\n")
    print(res)
else:

    print("Os valores fornecidos NÃO formam um triângulo.")