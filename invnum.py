"""
Escreva um programa em Python que lê um número inteiro positivo e
produz o número correspondente a inverter a ordem dos seus dígitos. Por
exemplo,
Escreva um inteiro positivo
? 7633256
O número invertido é 6523367
"""

lista = []
lista2 = []
if __name__ == '__main__':
    while True:
        try:
            numero = input('Digite um numero ')
            break
        except ValueError:
            print('Numero inválido')

    for x in numero:
        # print(x)
        lista.append(x)
    print("".join(lista))

    y = len(lista) - 1
    while not y < 0:
        # print(y)
        lista2.append(lista[y])
        y = y - 1
    print("".join(lista2))