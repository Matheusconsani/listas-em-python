t = 0
while 1:
    s = float(input("Digite o salário bruto (0 para sair): "))
    if s == 0:
        break
    h = float(input("Digite as horas trabalhadas: "))
    if s < 800:
        d = 0
    elif s <= 1600:
        d = s * 0.13
    else:
        d = s * 0.22
    if h > 160:
        e = (s / 160) * 0.5 * (h - 160)
    else:
        e = 0
    l = s - d + e
    t += l
    print("Salário líquido:", round(l, 2))
print("Total geral dos salários líquidos:", round(t, 2))
