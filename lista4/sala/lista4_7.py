a = []
for i in range(10):
    a.append(int(input(f"Digite o elemento {i+1}: ")))
b = a[::-1]
print("Matriz B:", b)
