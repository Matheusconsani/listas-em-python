a=int(input("Digite a primeira nota:"))
b=int(input("Digite a segunda nota:"))
if (a+b)/2>=6:
    print("Aluno aprovado com média ",(a+b)/2)
else:
    e=int(input("digite a nota de exame"))
    if (a+b+e)/3>=5:
        print("Aluno aprovado com média ",(a+b)/3)
    else:
        print("Aluno reprovado com média",(a+b+e)/3)
