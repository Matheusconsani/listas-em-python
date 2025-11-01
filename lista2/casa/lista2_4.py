a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
x = [a, b, c]
x.sort()
print("Maior número:", x[2])
print("Menor número:", x[0])
print("Número do meio:", x[1])
