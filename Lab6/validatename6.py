def validate_name(name):
    # Check if the name is a valid non-empty string
    if name.isalpha() and len(name) > 0:
        return True
    else:
        return False

def validate_age(age):
    # Check if the age is a valid number and greater than or equal to 18
    try:
        age = int(age)
        if age >= 18:
            return True
        else:
            return False
    except ValueError:
        return False

# Main Program
name = input("Enter your name: ")
age = input("Enter your age: ")

# Validate the name and age
if not validate_name(name):
    print("Invalid name. Name should contain only alphabets and must not be empty.")
else:
    if not validate_age(age):
        print("Invalid age. Age should be a number and you must be 18 or older to vote.")
    else:
        print(f"Hello {name}, you are eligible to vote." if int(age) >= 18 else f"Hello {name}, you are not eligible to vote.")
