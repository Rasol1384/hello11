import random


a = 1
b = 99


answer = int(input('My Answer to guess you: '))


guess = random.randint(a, b)
print('computer guess: ',guess)


guestion = input('guestion: ')


while guestion != 'd':
    if guestion == "b":
        a = guess + 1
        guess = random.randint(a, b)
        print(guess)
        guestion = input('guestion: ')
    elif guestion == "k":
        b = guess - 1
        guess = random.randint(a, b)
        print(guess)
        guestion = input('guestion:')
        
print('thanks your pc')        