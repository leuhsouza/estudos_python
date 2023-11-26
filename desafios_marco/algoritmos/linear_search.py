from random import randint

# minha_lista = []

# for n in range(0,10):
#     minha_lista.append (randint(0,10))

# print(minha_lista)
# pesquisado = int(input('Digite um valor a ser pesquisado: '))

def linear_search(lista,procurado):
    for indice, valor in enumerate(lista):
        if valor == procurado:
            return indice
    return -1

lista = [2, 3, 4, 10, 40]
x = 10         
resultado = linear_search(lista,x)
if resultado == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", resultado)
    
        
        #print(f'O valor procurado está na posição: {indice}')
    #return print('Valor não escontrado na lista')

# linear_search(minha_lista,pesquisado)