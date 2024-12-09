n = int(input("Enter the number of items in the dictionary:"))
dictionary = {}
for _ in range(n):
    key = input("Enter key:")
    value = int(input("Enter value:"))
    dictionary[key] = value


ascending = dict(sorted(dictionary.items(), key=lambda item: item[1]))
descending = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

print("Ascending:", ascending)
print("Descending:", descending)

