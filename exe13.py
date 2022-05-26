altura = float(input("Digite sua altura: "))
sexo = str(input("Digite 'M' para masculino e 'F' para feminino: ").upper())
if sexo == 'M':
    print("O seu peso ideal é: {:.2f}".format((72.7*altura)-58))

if sexo == 'F':
    print("O seu peso ideal é: {:.2f}".format((62.1*altura)-44.7))



