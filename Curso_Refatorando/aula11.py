
try:
    numero = int(input("Digite um Numero: "))
    print(numero)

    10/0
except ZeroDivisionError:
    print ("Divisão por zero não é possivel")
except ValueError:
    print ("digite um valor valido.")
except:
    print("erro inexperado.")

finally:
    print("sempre executa" )