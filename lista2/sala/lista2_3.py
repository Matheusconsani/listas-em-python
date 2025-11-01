a=int(input("Digite o primeiro valor:"))
b=int(input("Digite o segundo valor:"))
if a>b:
    b=a-b
else:
    b=b-a

print("A diferença é:",b)