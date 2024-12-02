# Accept file name from the user
file_name = input("Enter the file name: ")

# Get the extension of the file
extension = file_name.split('.')[-1]

# Output the extension
print(f"The extension of the file is: {extension}")
