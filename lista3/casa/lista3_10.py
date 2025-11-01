while True:
    o = input("Digite '+', '-', '*', '/', ou 'S' para sair: ")
    if o.upper() == 'S':
        break
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    if o == '+':
        r = a + b
    elif o == '-':
        r = a - b
    elif o == '*':
        r = a * b
    elif o == '/':
        r = a / b
    else:
        print("Operação inválida")
        continue
    print("Resultado:", r)
