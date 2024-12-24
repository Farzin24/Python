num1 = float(input("enter the 1st number: "))
num2 = float(input("enter the 2nd number: "))
num3 = float(input("enter the 3rd number: "))

if num1 > num2 and num1 > num3:
    print("the biggest is", num1)
elif num2 > num1 and num2 > num3:
    print("the biggest is:", num2)
else:
    print("the biggest is:", num3)


