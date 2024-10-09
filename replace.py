s=input("Enter a string:")
first_char=s[0]
modified_string=first_char+s[1:].replace(first_char,'$')
print("modified string:",modified_string)
