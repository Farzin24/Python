n = int(input("Enter the number of terms to display powers of 2: "))
powers_of_2 = list(map(lambda x: 2 ** x, range(n)))
print("Powers of 2:", powers_of_2)


