print("Calculadora de média aritimética.")
quantidades_n = int(input("Digite a quatidade de números para média: "))
x = quantidades_n
lista = []


while quantidades_n > 0:
    quantidades_n -= 1
    ordem = x - quantidades_n
    n = float(input("Digite o {}º número: ".format(ordem)))
    lista.append(n)

media = sum(lista)/x

print("A média aritmética é: {:.2f}".format(media))

