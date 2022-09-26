"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido
- O maior valor inserido
- A média das vendas
"""

listaVendas = [100, 50, 200, 300, 400]
listailhas = ['Terceira', 'Pico', 'Faial', 'São Jorge', 'Graciosa']

soma = sum(listaVendas)
minimo = min(listaVendas)
maximo = max(listaVendas)
print(f'Mínimo Valor {minimo}')
print(f'Máximo Valor {maximo}')
print(f'Total de Vendas {soma}')

