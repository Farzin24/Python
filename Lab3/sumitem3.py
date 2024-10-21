numbers=[int (x) for x in input("enter numbers (seprated by spaces):").split()]
total_sum=0
for num in numbers:
    total_sum += num
print(f"the sum of all item in the list is:{total_sum}")
