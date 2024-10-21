
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))


def all_even_digits(num):
    return all(int(digit) % 2 == 0 for digit in str(num))


def is_perfect_square(num):
    sqrt = int(num ** 0.5)
    return sqrt * sqrt == num


even_digit_squares = []
for num in range(start, end + 1):
    if is_perfect_square(num) and all_even_digits(num):
        even_digit_squares.append(num)


print("Four-digit even digit perfect squares:", even_digit_squares)

