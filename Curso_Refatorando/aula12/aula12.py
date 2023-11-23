#open("caminho", "r")
#Mode
#r - leitura
#a - Append / Incrementar
# w - Escrita
# x - Criar Arquivo
# r+ - Leitura + Escrita

# arquivo = open("Curso_Refatorando/aula12/test3.txt","w")

# print(arquivo.readable())
# print(arquivo.read())
# print(arquivo.readline())

# lista = arquivo.readlines()
# print(lista)

# print(lista[3])


#arquivo.write("Python\n")



#arquivo.close()

import os

if os.path.exists("Curso_Refatorando/aula12/test2.txt"):
    os.remove("Curso_Refatorando/aula12/test2.txt")
else :
    print("Arquivo não existe")

os.rmdir("Curso_Refatorando/aula12/nova_pasta")

#necessário a pasta estar vazia para remove-la