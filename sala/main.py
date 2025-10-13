t= float(input("Digite o tempo gasto na viagem (EM HORAS):"))
vm=float(input("Digite a velocidade média durante a viagem durante a viagem(em km/h:)"))

d=t*vm
lu=d/12
4
print("\n")
print("Velocidade média:", vm, "km\h")
print("Tempo gasto na viagem:", t, "horas")
print("Distancia Percorrida:",d,"km")
print("Quantidade de litros usados na viagem:",'%.2f' %lu,"litros")