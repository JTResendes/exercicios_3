def frase_lista(frase):
    frase_list = frase.split()

    return frase_list


if __name__ == '__main__':
    frase = input('Insira a sua frase: ')
    palavra = input('Insira a palavra para substituir a outra: ')
    mudar = input('Insira a palavra para substituir: ')

    if palavra in frase_lista(frase):
        frase = frase_lista(frase)
        for x in range(len(frase)):
            if frase[x] == palavra:
                frase[x] = mudar
        frase = ' '.join(str(x) for x in frase)
        print(frase)
    else:
        print('A palavra nao está na frase.')
