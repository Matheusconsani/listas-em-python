c = int(input("Digite o código do curso (1 a 5): "))
d = {1:"Engenharia",2:"Edificações",3:"Sistemas Elétricos",4:"Turismo",5:"Análise de Sistemas"}
print("Curso:", d.get(c,"Código inválido"))
