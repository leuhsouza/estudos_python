from random import randint

search = int(input('Digite um numero para pesquisa-lo: '))

minha_lista = []

for n in range (0,10):
    minha_lista.append (randint(0,10))

minha_lista.sort()

print(minha_lista)

inicio = 0
fim = len(minha_lista) - 1

encontrado = False
meio = 0

while inicio <= fim:
    meio = (inicio + fim) // 2
    valor_meio = minha_lista[meio]
    if valor_meio == search:
        encontrado = True
        break
    elif valor_meio < search:
        inicio = meio + 1
    else:
        fim = meio -1

if encontrado:
    print(f"Elemento {search} encontrado no índice {meio}.")
else:
    print(f"Elemento {search} não encontrado na lista.")



#mid = len(minha_lista)[0] + (len(minha_lista)[-1] - len(minha_lista[0])) /2
