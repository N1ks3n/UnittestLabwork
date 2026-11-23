import argparse

def area(width, height):
    return width * height

def perimeter(width, height):
    return 2 * (width + height)

width = float(input("Ширина: "))
height = float(input("Высота: "))

print("Площадь: " + str(area(width, height)))
print("Периметр: " + str(perimeter(width, height)))