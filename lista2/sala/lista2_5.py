try:
    A = float(input("Digite o primeiro valor:"))
    B = float(input("Digite o segundo valor:"))
    C = float(input("Digite o terceiro valor:"))
    v = [A,B,C]
    vo = sorted(v)
    print("\n")
    print("Valores em ordem crescente:")
    print(vo)
except ValueError:
    print("\nERRO digite apenas números válidos.")