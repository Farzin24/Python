def compare(s1, s2, n):
    return s1[:n] == s2[:n]

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
n = int(input("Enter the number of characters to compare: "))
result = compare(s1, s2, n)
print("Result of comparison:", result)

