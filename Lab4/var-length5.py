def add_numbers(*args):
    return sum(args)
user_input=input("enter the numbers seprated by spaces:")
numbers=list(map(int,user_input.split()))
result=add_numbers(*numbers)
print("sum of numbers:",result)

