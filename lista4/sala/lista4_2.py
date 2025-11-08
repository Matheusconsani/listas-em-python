import math

a = []
for i in range(6):
    n = int(input(f"Digite o elemento {i+1}: "))
    a.append(n)
b = [math.factorial(x) for x in a]
print("Matriz B:", b)
