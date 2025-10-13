ap=int(input("Digite o valor da altura da parede:"))
lp=int(input("Digite o valor da largura da parede:"))
aa=int(input("Digite o valor da altura do azuleijo:"))
la=int(input("Digite o valor da largura do azuleijo:"))

aaz=aa*la
apa=ap*lp

n=apa/aaz

print("Para azuleijar a parede são necessarios ",n, "Azuleijos")