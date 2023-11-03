from random import randint

lista = []

for n in range(0,10):
    lista.append (randint(0,10))


print (lista)

procurado = int(input('Digite um valor a ser pesquisado: '))

def linear_search(lista,procurado):
for indice, valor in enumerate(lista):
    if valor == procurado:
        return f'O valor procurado está na posição: {indice}'
    return 'Valor não escontrado na lista'


    
    '''if procurado == valor:
        print(f'O valor procurado está na posição {indice}')
    else'''