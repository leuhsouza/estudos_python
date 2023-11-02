class Carro:
    pass

meu_carro = Carro()

carro_do_leo = Carro()

meu_carro.ano = 1968
meu_carro.modelo = 'Fusca'
meu_carro.cor = 'Azul'

print(meu_carro.ano)

print (meu_carro.cor)


carro_do_leo.ano = 1981
carro_do_leo.modelo = 'Brasilia'
carro_do_leo.cor = 'Preto'

print (carro_do_leo.modelo)

novo_carro = meu_carro

novo_carro.ano +=10

print(meu_carro.ano)
print(novo_carro.ano)