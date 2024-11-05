def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

N = int(input("Enter the number of terms in the Fibonacci series: "))  # Fixed closing parenthesis
print("Fibonacci series:")
for i in range(N):
    print(fibonacci(i), end=" ")

