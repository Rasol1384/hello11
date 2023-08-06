N=input("whats your name?")
G=input("whats your guess?")
G=int(G)
import random
C=random.randint(1,99)
while   C!=G:
    if   G>C:
        print("your guess is bigger than mine")
    else:
        print("your guess is smaller than mine")
    G=input("whats your guess?")
    G=int(G)
print("congratulations",N,"you did it")       
