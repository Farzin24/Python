
n = int(input("Enter a number to check if it's an Armstrong number: "))


original_n = n
sum = 0


while n > 0:
    digit = n % 10
    sum += digit ** 3
    n = n // 10


if sum == original_n:
    print(f"{original_n} is an Armstrong number.")
else:
    print(f"{original_n} is not an Armstrong number.")

