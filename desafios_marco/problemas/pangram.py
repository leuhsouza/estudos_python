def verifica_pangrama(frase):
    frase = frase.lower()

    letras_presentes = set()

    for char in frase:
        if char.isalpha():
            letras_presentes.add(char)

    alfabeto = set("abcdefghijklmnopqrstuvwxyz")
    return letras_presentes == alfabeto

frase_exemplo = "Um pequeno jabuti xereta viu dez cegonhas felizes."

resultado = verifica_pangrama(frase_exemplo)

if resultado:
    print("A frase é um pangrama!")
else:
    print("A frase não é uma pangrama.")