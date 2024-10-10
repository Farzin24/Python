numbers=[int(x) for x in input("Enter a list of integers (space-seperated):").split()]
odd_numbers=[num for num in numbers if num %2 !=0]
print("List after removing even numbers:",odd_numbers)

