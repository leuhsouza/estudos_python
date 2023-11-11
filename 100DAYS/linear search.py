from random import randint

minha_lista = []

for n in range(0,10):
    minha_lista.append (randint(0,10))

print(minha_lista)
pesquisado = int(input('Digite um valor a ser pesquisado: '))

def linear_search(lista,procurado):
    for indice, valor in enumerate(lista):
        if valor == procurado:
            return print(f'O valor procurado está na posição: {indice}')
    return print('Valor não escontrado na lista')


linear_search(minha_lista,pesquisado)
    
