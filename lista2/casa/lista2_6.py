m = int(input("Digite o número do mês (1 a 12): "))
d = {1:"Janeiro",2:"Fevereiro",3:"Março",4:"Abril",5:"Maio",6:"Junho",7:"Julho",8:"Agosto",9:"Setembro",10:"Outubro",11:"Novembro",12:"Dezembro"}
print("Mês:", d.get(m,"Inválido"))
