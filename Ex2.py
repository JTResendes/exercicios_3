"""
Peça ao utilizador para inserir uma frase
Após o utilizador ter inderido a frase apresente:
 - Qual é o comprimento da frase inserida (incluindo espaços)
 - Quantas palavras tem a frase
 - Quantas vogais tem a frase
 - Quantas letras maiusculas tem a frase
 - Quantas letras minusculas tem a frase
 - Quantos numeros tem a frase
 - Apresente a frase invertida. Exemplo: A frase é 'Bom dia!' deve dar '!aid moB'
"""
import re

frase = "Boas tardes"


def contar_letras(string):
    qtt_minus = 0
    qtt_maisc = 0

    for i in range(len(string)):
        if string[i].islower():
            qtt_minus += 1
        elif string[i].isupper():
            qtt_maisc += 1

    return qtt_minus, qtt_maisc


count_chars = {}
for char in frase:
    if char not in count_chars:
        count_chars[char] = 0
    count_chars[char] += 1

for char in count_chars:
    print('A Frase tem {} {}'.format(count_chars[char], char))

comprimento = len(frase)
palavras = len(frase.split())
qtt_minus, qtt_maisc = contar_letras(frase)
print("Quantidade de letras minúsculas: %d" % qtt_minus)
print("Quantidade de letras maiúsculas: %d" % qtt_maisc)

print(f'Palavras: {palavras}')
print(f'Comprimento: {comprimento}')
# https://acervolima.com/programa-python-para-calcular-o-numero-de-palavras-e-caracteres-na-string/
