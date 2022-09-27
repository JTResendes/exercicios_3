"""
Peça ao utilizador para inserir uma frase
Após o utilizador ter inderido a frase apresente:
 - Imprima a frase, mas com cada palavra invertida. Por exemplo 'Bom dia!' deve dar 'moB !aid'
 - Imprima a frase, mas com as maiusculas em minisculo e as minusculas em maiusculas.
 - Quantas palavras tem a frase
 - Quantas vogais tem a frase
 - Quantas letras maiusculas tem a frase
 - Quantas letras minusculas tem a frase
 - Quantos numeros tem a frase
 - Apresente a frase invertida. Exemplo: A frase é 'Bom dia!' deve dar '!aid moB'
"""
if __name__ == '__main__':
    frase = input('Insira frase:')

    palavras = frase.split(' ')
    num_vogais = 0
    maiusculas = 0
    minusculas = 0
    numeros = 0

    vogais = 'aeiou'
    for char in frase:
        if char in vogais:
            num_vogais += 1
        if char.isalpha() and char != '':
            if char.islower():
                minusculas += 1
            else:
                maiusculas += 1
        elif char.isalnum():
            numeros += 1
    invertida = ' '.join(palavra[::-1] for palavra in frase.split())
    print(invertida)
    print(f'Comprimento:{len(frase)}')
    print(f'Palavras:{len(palavras)}')
    print(f'Vogais {num_vogais}')
    print(f'Maiusculas {maiusculas}')
    print(f'Minusculas {minusculas}')
    print(f'Números {numeros}')
    frase = frase[::-1]
    print(frase)
