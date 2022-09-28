if __name__ == '__main__':
    lista_de_caracteres = ['.', '!', '?']
    frase = ''
    x = 0
    while x < 10:
        frase = str(input('Digite uma frase com mais de 10 caracteres: '))
        x = len(frase)
        y = x - 1
        if x < 10:
            print('A frase tem que ter mais de 10 caracteres.')

        elif frase[y] in lista_de_caracteres:
            print('', end='')
        else:
            print('A frase tem que terminar com um deste pontos ".", "!", "?".')
            x = 0
#tirar dúvida sobre caracteres siguidos