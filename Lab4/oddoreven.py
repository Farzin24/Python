def is_even(number):
    return number % 2==0
number=int(input("enter a number:"))
if is_even(number):
    print("the number is even.")
else:
    print("the number is odd.")
