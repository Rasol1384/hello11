num=input("please give me your number: ")
if    len(num)!=2:
    print("your must enter 2 digits!")
    quit()
elif    not    num.isdigit():
        print('Your input must be a number!')
        quit()
num=int(num)
number= str(num%10) + str(num//10)
#number2=int(number)*2
print(number)
      