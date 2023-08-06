import random
C=random.randint(1,99)
N=input("whats your name?")
G=int(input("whats your guess?"))
while   G!=C:
    if  G>C:
        print("your guess is bigeer than mine")
    else:
        print("your guess is smaller than mine")
    G=int(input("whats your guess?"))
print("ohhhhh my god",N,"your guess is true")