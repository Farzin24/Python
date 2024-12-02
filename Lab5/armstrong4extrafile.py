def is_armstrong(number):
    digits = [int(d) for d in str(number)]
    power = len(digits)
    return number == sum(d ** power for d in digits)

