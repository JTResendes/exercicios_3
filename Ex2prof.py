import random

'''if __name__ == '__main__':
    total = 0
    num1 = int(input('Insere primeiro numero '))

    num2 = int(input('Insere segundo numero'))

for x in range(num1, num2 + 1):
    total = num1 + num2
print(f' A soma será {total}')


'''


def comfor(num1, num2):
    soma = 0
    for n in range(num1, num2 + 1):
        soma += n

    return soma


def comwhile(num1, num2):
    soma = 0
    n = num1
    while n <= num2:
        soma += n
        n += 1

    return soma


if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        primeirov = int(input('Insira o primeiro numero '))
        segundov = int(input('Insira o segundo numero '))
        fuc = input(' Usar comwhile ou comfor?')

        while True:

            if fuc == 'comfor':
                print(comfor(primeirov, segundov))
                break
            elif fuc == 'comwhile':
                print(comwhile(primeirov, segundov))
                break
        continuar = input('Repetir [s | n]? ')
    print(f'Adeus!')
