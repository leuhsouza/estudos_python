# def big_mac():
#     print("sanduiche big mac")


# print('inicio')
# big_mac()
# print("fim")

def fazer_big_mac(nome):
    print(f"sanduiche big mac {nome}")

# fazer_big_mac('Roger')
# fazer_big_mac('Cris')
# fazer_big_mac("Manu")

def fazer_batata(tamanho):
    print(f'batata {tamanho}')

def preparar_refrigenante(tipo, tamanho):
    print(f"{tipo} {tamanho}")

# fazer_big_mac("Leonardo")
# fazer_batata("Grande")
# preparar_refrigenante("Coca", "Média")

def combo_bigmac(nome,tamanho_batata,tipo_refri,tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigenante(tipo_refri,tamanho_refri)

#combo_bigmac("Leonardo", "Grande", "Coca" , "Média")

def soma_num(num1,num2):
    return num1 + num2

resultado = soma_num(15,20)
#print(resultado)

def maior_num (lista_num):
    lista_num.sort()
    lista_num.reverse()
    maior_num = lista_num[0]
    return maior_num

resultado = maior_num([1,634,74,364,3,674,-645, 366])
print(resultado)