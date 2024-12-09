input_string=input("enter a string:")
frequency={}
for char in input_string:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1
print(frequency)
