ganho_hora = float(input("Digite quanto ganha por hora: "))
hora_trabalhada = int(input("Digite quantas horas trabalhou: "))
print("Você ganha R${:.2f} por hora e trabalhou {} horas. O seu salário é de: R${:.2f}".format(ganho_hora, hora_trabalhada, ganho_hora*hora_trabalhada))
