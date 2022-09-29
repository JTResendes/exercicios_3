# 5 numeros e 2 estrelas, bónus caso esteja ordenado de forma crescente, 50 numeros e 12 estrelas, 5 apostas
from random import random

listaN = [0, 0, 0, 0, 0]
listaE = [0, 0]


def get_random(ini, fim):
    """
    Esta função devolve um número aleatório entre ini e fim inclusive
    :param ini: inicío do intervalo
    :param fim: fim do intervalo
    :return: número aleatório
    """
    return random.randrange(ini, fim + 1)

    for x in range(listaN, listaE + 1):
        num_random = get_random(listaN, listaE)
        list_random.insert(x, num_random)



