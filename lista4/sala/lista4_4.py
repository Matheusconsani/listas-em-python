a = []
b = []
for i in range(5):
    a.append(int(input(f"Digite o elemento {i+1} de A: ")))
for i in range(5):
    b.append(int(input(f"Digite o elemento {i+1} de B: ")))
c = a + b
print("Matriz C:", c)
