from random import randint
lista = []
for c in range (0,10):
    lista.append(randint(0,20))


print(lista)


n = len(lista)

for i in range(n):
    swapped = False

    for j in range(0,n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
            swapped = True
    if (swapped == False):
        break

print(lista)