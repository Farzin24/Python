area_square = lambda side: side * side
area_rectangle = lambda length, width: length * width
area_triangle = lambda base, height: 0.5 * base * height

side = float(input("Enter the side length of the square: "))
print("Area of square:", area_square(side))

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print("Area of rectangle:",area_rectangle(length,width))

base = float(input("Enter the base of triangle: "))
height = float(input("Enter the height of triangle: "))
print("Area of triangle:", area_triangle(base,height))

