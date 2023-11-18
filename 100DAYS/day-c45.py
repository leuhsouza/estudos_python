names = ['Harry', 'James', 'Jack']#names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

from random import randint
""""
n = randint(0,len(names))
print(n)
print(len(names)+1)
print(f'{names[n]} is going to buy the meal today!')"""

num_items = len(names)

random_choice = randint(0,num_items -1)

person = names[random_choice]

print(person)