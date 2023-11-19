familia = ['Leonardo', 'Isabela' , 'Luisa' , 'Jessica']

#print(familia[-4])
#print(familia[2:])
#print(familia[1:3])

#familia [3] = 'Roger'
#print(familia)

familia.extend(['Irene', 'Matheus']) #adicionando outra lista
print(familia)

#familia.append('Rebeca')
familia.insert(2,'Rebeca')
print(familia)
familia.pop() # excluir ultimo registro
familia.remove('Rebeca')
print(familia)

#familia.clear

#print(familia.index('Jessica'))
#print(familia.count('Leonardo'))

idade_familia = [29,29,9,2,15]
#idade_familia.sort()

#print(idade_familia)

idade_familia.sort()
idade_familia.reverse()
print(idade_familia)

#familia2 = familia
familia2 = familia.copy()
familia.remove('Leonardo')

print(familia)
print(familia2)
#copia com referencia
