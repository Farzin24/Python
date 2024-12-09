class Time:
    def __init__(self, hour, minute, second):
        # Initialize the private attributes
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __str__(self):
        # String representation of Time object
        return f"{self.__hour:02}:{self.__minute:02}:{self.__second:02}"

    def __add__(self, other):
        # Overload the '+' operator to add two Time objects
        if isinstance(other, Time):
            # Adding hours, minutes, and seconds
            total_seconds = self.__to_seconds() + other.__to_seconds()
            
            # Converting total seconds back to hours, minutes, and seconds
            hour = (total_seconds // 3600) % 24
            minute = (total_seconds % 3600) // 60
            second = total_seconds % 60
            
            return Time(hour, minute, second)
        else:
            raise TypeError("The operand must be an instance of Time")

    def __to_seconds(self):
        # Convert time to total seconds
        return self.__hour * 3600 + self.__minute * 60 + self.__second

# Function to take input for Time
def get_time_input():
    hour = int(input("Enter hour: "))
    minute = int(input("Enter minute: "))
    second = int(input("Enter second: "))
    return Time(hour, minute, second)

# Main Program
print("Enter the first time:")
time1 = get_time_input()

print("Enter the second time:")
time2 = get_time_input()

# Add the two Time objects
result = time1 + time2

# Output the result
print(f"The sum of the two times is: {result}")
