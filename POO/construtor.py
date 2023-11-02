#construtor para definir valores iniciais e parametros"
class Carro:
    def __init__(self,modelo,ano,cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

carro_do_meu_tio = Carro('Lamborghini', 2023,'Amarela')

print(carro_do_meu_tio.modelo)
                 