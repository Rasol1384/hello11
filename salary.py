def salary(hour,pay):
    if    hour>8:
        return "You will not be paid because you have worked more than the legal limit"
    sum=(hour*pay)
    return sum
pay1=int(input("Please Enter Your Pay: "))
hour1=int(input("Please Enter How Many Hour Do You Work: "))
print(salary(hour1,pay1))
