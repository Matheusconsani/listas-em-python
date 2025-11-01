n = float(input("Digite a nota do aluno: "))
i = int(n)
d = n - i
if d > 0.5:
    r = i + 1
else:
    r = i
print("Nota arredondada:", r)
