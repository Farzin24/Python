number=int(input("enter a number:"))
factorial=1
for i in range(2,number+1):
    factorial *=i
print(f"the factorial of{number} is {factorial}")
