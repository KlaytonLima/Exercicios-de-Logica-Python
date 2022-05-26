n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = float(input("Digite um número real: "))
a = (n1*2)+(n2/2)
b= (n1*3)+n3
c= n3**3
print("O dobro de {} é {} + a metade de {:.0f} é {:.0f} somados o resultado é: {:.0f}".format(n1, n1*2, n2, n2/2, a))
print("O triplo de {} é {} somado com {} fica no valor de: {}".format(n1, n1*3, n3, b))
print("O número {} elevado ao cubo fica no valor de: {:.2f}".format(n3, c))
