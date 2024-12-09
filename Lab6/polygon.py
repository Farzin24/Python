from abc import ABC, abstractmethod

# Abstract class Polygon
class Polygon(ABC):
    # Abstract method to calculate area
    @abstractmethod
    def calculate_area(self):
        pass

    # Abstract method to get the details of the dimensions
    @abstractmethod
    def get_details(self):
        pass

# Rectangle class derived from Polygon
class Rectangle(Polygon):
    def __init__(self):
        self.length = 0
        self.breadth = 0

    # Method to get the dimensions of the rectangle from the user
    def get_details(self):
        self.length = float(input("Enter the length of the rectangle: "))
        self.breadth = float(input("Enter the breadth of the rectangle: "))

    # Method to calculate the area of the rectangle
    def calculate_area(self):
        return self.length * self.breadth

# Triangle class derived from Polygon
class Triangle(Polygon):
    def __init__(self):
        self.base = 0
        self.height = 0

    # Method to get the dimensions of the triangle from the user
    def get_details(self):
        self.base = float(input("Enter the base of the triangle: "))
        self.height = float(input("Enter the height of the triangle: "))

    # Method to calculate the area of the triangle
    def calculate_area(self):
        return 0.5 * self.base * self.height

# Main program to interact with the user
def main():
    # Ask user which polygon they want to calculate the area for
    polygon_type = input("Enter the type of polygon (Rectangle/Triangle): ").strip().lower()

    if polygon_type == "rectangle":
        rectangle = Rectangle()
        rectangle.get_details()  # Get the rectangle dimensions from the user
        print(f"The area of the rectangle is: {rectangle.calculate_area()} square units.")
    elif polygon_type == "triangle":
        triangle = Triangle()
        triangle.get_details()  # Get the triangle dimensions from the user
        print(f"The area of the triangle is: {triangle.calculate_area()} square units.")
    else:
        print("Invalid polygon type! Please enter 'Rectangle' or 'Triangle'.")

if __name__ == "__main__":
    main()
