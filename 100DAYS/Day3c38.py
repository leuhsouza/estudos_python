"""print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇



T = name1.lower().count('t') + name2.lower().count('t')
R = name1.lower().count('r') + name2.lower().count('r')
U = name1.lower().count('u') + name2.lower().count('u')
E = name1.lower().count('e') + name2.lower().count('e')


true = T+R+U+E

L = name1.lower().count('l') + name2.lower().count('l')
O = name1.lower().count('o') + name2.lower().count('o')
V = name1.lower().count('v') + name2.lower().count('v')
E = name1.lower().count('e') + name2.lower().count('e')

love = L+O+V+E

score = true + love

if score <10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif 40 <= score <= 50:
    print(f'Your score is {score}, you are alright together. ')
else:
    print(f'Your score is {score}.')"""


print("The Love Calculator is calculating your score...")
name1 = input()  
name2 = input()  

T = name1.lower().count('t') + name2.lower().count('t')
R = name1.lower().count('r') + name2.lower().count('r')
U = name1.lower().count('u') + name2.lower().count('u')
E = name1.lower().count('e') + name2.lower().count('e')

true = T + R + U + E

L = name1.lower().count('l') + name2.lower().count('l')
O = name1.lower().count('o') + name2.lower().count('o')
V = name1.lower().count('v') + name2.lower().count('v')
E = name1.lower().count('e') + name2.lower().count('e')

love = L + O + V + E

print(f'True: {true}, Love: {love}')  # Adicionando esta linha para depuração

score = true * 10 + love

if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif 40 <= score <= 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')