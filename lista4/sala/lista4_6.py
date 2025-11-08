a = []
for i in range(8):
    a.append(int(input(f"Digite o elemento {i+1}: ")))
b = [x**2 for x in a]
print("Matriz B:", b)

s = sum(b)
m = s / len(b)
maior = max(b)
menor = min(b)

print("Soma dos elementos de B:", s)
print("Média dos elementos de B:", m)
print("Maior elemento de B:", maior)
print("Menor elemento de B:", menor)
