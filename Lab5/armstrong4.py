from Armstrong import is_armstrong

def find_armstrong_numbers(start, end):
    return [num for num in range(start, end + 1) if is_armstrong(num)]


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
armstrong_numbers = find_armstrong_numbers(start, end)
print("Armstrong numbers between", start, "and", end, "are:", armstrong_numbers)


