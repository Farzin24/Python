integers = [int(x) for x in input("Enter a list of integers (space-separated): ").split()]


word = input("Enter a word: ")


positive_numbers = [num for num in integers if num > 0]


squared_numbers = [num ** 2 for num in integers]


vowels = [char for char in word if char in 'aeiouAEIOU']


ordinal_values = [ord(char) for char in word]


print("\n(a) Positive numbers from the list:", positive_numbers)
print("(b) Squares of the numbers:", squared_numbers)
print("(c) Vowels in the word:", vowels)
print("(d) Ordinal values of each character in the word:", ordinal_values)

