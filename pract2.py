import math


def squareRootCalculator():
    num = float(input("Enter a non-negative number: "))
    if num < 0:
        print("Square root is undefined for negative numbers.")
    else:
        sqrtValue = math.sqrt(num)
        print("Square root:", round(sqrtValue, 2))


def sineAndCosine():
    angle = float(input("Enter an angle in degrees: "))
    angleInRadians = math.radians(angle)  # converts degrees to radians
    sineValue = math.sin(angleInRadians)
    cosineValue = math.cos(angleInRadians)
    print("Sine of the angle:", round(sineValue, 2))
    print("Cosine of the angle:", round(cosineValue, 2))


# Add your solutions to the programming exercises here.
# Remember that the `math` module is already imported for you (do not import it again!)
