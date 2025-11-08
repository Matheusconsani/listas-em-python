a = []
for i in range(5):
    n = int(input(f"Digite o elemento {i+1}: "))
    a.append(n)
b = [x * 3 for x in a]
print("Matriz B:", b)

