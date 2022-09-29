# Sortear 5 numeros situados em 1 e 50 detro da lista
from random import random

lista = [0, 0, 0, 0, 0]


def get_random(ini, fim):
    """
    Esta função devolve um número aleatório entre ini e fim inclusive
    :param ini: inicío do intervalo
    :param fim: fim do intervalo
    :return: número aleatório
    """
    return random.randrange(ini, fim + 1)


if __name__ == '__main__':
    nums = [0, 0, 0, 0]
    for x in range(len(nums)):
        nums[x] = get_random(1, 5)
    print(nums)
