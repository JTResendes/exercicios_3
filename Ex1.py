"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido
- O maior valor inserido
- A média das vendas
FUNÇÕES GLOBAIS - FORA DA FUNÇÃO
"""

print(f'Insira 5 dados')
listaVendas = [int(input()) for c in range(5)]  # 100, 50, 200, 300, 400 f'Insira {ndados -1} valores inteiros'
soma = listaVendas.__len__()
listailhas = ['Terceira', 'Pico', 'Faial', 'São Jorge', 'Graciosa']
media = sum(listaVendas) / soma
soma = sum(listaVendas)
minimo = min(listaVendas)
maximo = max(listaVendas)

print(f'Mínimo Valor {minimo}')
print(f'Máximo Valor {maximo}')
print(f'Total de Vendas {soma}')
print(f'Média {media}')