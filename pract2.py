from math import *


def heightOfTriangle():
    base = float(input("Enter base: "))
    angleInDegrees = float(input("Enter angle: "))

    angleInRadians = radians(angleInDegrees)
    height = base * tan(angleInRadians)
    print("Height of triangle: ", round(height, 2))


def distanceBetweenPoints():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("Distance between points: ", round(distance, 2))

# TODO: Add your solutions to the programming exercises here.
# Remember that the `math` module is already imported for you (do not import it again!)
