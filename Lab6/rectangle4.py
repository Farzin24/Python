class Rectangle:
    def __init__(self, length, breadth):
        # Initializing the length and breadth of the rectangle
        self.length = length
        self.breadth = breadth

    def area(self):
        # Method to calculate the area of the rectangle
        return self.length * self.breadth

    def perimeter(self):
        # Method to calculate the perimeter of the rectangle
        return 2 * (self.length + self.breadth)

    def compare_area(self, other_rectangle):
        # Method to compare the area of two rectangles
        if self.area() > other_rectangle.area():
            return "The first rectangle has a larger area."
        elif self.area() < other_rectangle.area():
            return "The second rectangle has a larger area."
        else:
            return "Both rectangles have the same area."

# Main program to interact with the user
def main():
    # Get input for the first rectangle
    length1 = float(input("Enter the length of the first rectangle: "))
    breadth1 = float(input("Enter the breadth of the first rectangle: "))
    rect1 = Rectangle(length1, breadth1)

    # Get input for the second rectangle
    length2 = float(input("Enter the length of the second rectangle: "))
    breadth2 = float(input("Enter the breadth of the second rectangle: "))
    rect2 = Rectangle(length2, breadth2)

    # Calculate and display the area and perimeter of the first rectangle
    print(f"\nArea of the first rectangle: {rect1.area()} square units")
    print(f"Perimeter of the first rectangle: {rect1.perimeter()} units")

    # Calculate and display the area and perimeter of the second rectangle
    print(f"\nArea of the second rectangle: {rect2.area()} square units")
    print(f"Perimeter of the second rectangle: {rect2.perimeter()} units")

    # Compare the two rectangles by area
    print(f"\nComparison of areas: {rect1.compare_area(rect2)}")

if __name__ == "__main__":
    main()
