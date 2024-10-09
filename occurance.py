names=input("Enter first names seperated by spaces:").split()
count_a=sum([name.lower().count('a')
    for name in names])
print("Occurences of 'a':",count_a)

