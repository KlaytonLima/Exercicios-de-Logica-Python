salario_hora = float(input("Digite quanto ganha por hora: "))
hora_trabalhada = int(input("Digite quantas horas trabalhou: "))
salario_bruto = salario_hora*hora_trabalhada
ir = salario_bruto-11/100
inss = ir-8/100
sindicato = inss-5/100
salario_liquido = salario_bruto-24/100
print("-----------------------------------------------")
print("Salario bruto: R$ {:.2f}".format(salario_bruto))
print("IR (11%): R$ {:.2f}".format(ir))
print("INSS (8%): R$ {:.2f}".format(inss))
print("Sindicato (5%): R$ {:.2f}".format(sindicato))
print("-----------------------------------------------")
print("Salário Liquido: R$ {:.2f}".format(salario_liquido))
print("-----------------------------------------------")
