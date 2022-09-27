"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido assim como as respetivas ilhas
- O maior valor inserido assim como as respetivas ilhas
- A média das vendas
//zip
"""


ilhas = ['Terceira', 'Graciosa', 'Pico', 'Faial', 'São Jorge']

if __name__ == '__main__':
    vendas = []
    for ilha in ilhas:
        vendas.append((int(input(f'Insira as vendas para {ilha} '))))
    print(f'vendas = {vendas}')
    print(f'Total Vendas = {sum(vendas)}')

    menor1 = vendas[0]
    maior1 = vendas[0]
    for x in range(1, len(vendas)):
        if vendas[x] < menor1:
            menor = vendas[x]
        if vendas[x] > maior1:
            maior1 = vendas[x]
            if maior1

    print(f'O maior é {maior1} ilha {ilhas}.')

