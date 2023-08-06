def salari(hour,pay_hour):
    if hour>8:
        return "you to much work!" 
    else:
        total_salari=hour*pay_hour
        return total_salari
new_var = int(input("hour:"))
new_var1 = int(input("pay_hour:"))
print(salari(new_var,new_var1))