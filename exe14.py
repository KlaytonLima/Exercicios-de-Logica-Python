kg_peixe = float(input("Digite o kg do peixe: "))
exesso= kg_peixe-50
multa = float (4.00)
print("Exedeu {:.1f}Kg de peixe. Com a multa de R$ {:.2f} o Kg, o valor do exesso fica R$ {:.2f}".format(exesso, multa,exesso*multa))
