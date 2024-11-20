import calendar
def is_leap_year(year):
    return calendar.isleap(year)

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
