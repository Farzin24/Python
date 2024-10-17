n = int(input("Enter the number of terms for the Fibonacci series: "))
a, b = 0, 1
fib_series = []
for i in range(n):
    fib_series.append(a)
    a, b = b, a + b

print(f"Fibonacci series of {n} terms: {fib_series}")

