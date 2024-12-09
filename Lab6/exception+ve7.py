def check_number(number):
    # Check if the number is positive or zero
    if number >= 0:
        print(f"The entered number is: {number}")
    else:
        # Raise ValueError if the number is negative
        raise ValueError("The number cannot be negative!")

# Main program
try:
    # Prompt user to enter a number and convert it to a float to handle both integer and decimal inputs
    number = float(input("Enter a number: "))
    check_number(number)  # Check the number
except ValueError as ve:
    # Handle ValueError and print the error message
    print(f"Error: {ve}")
