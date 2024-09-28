import math

def square_root_calculator():
    num = float(input("Enter a non-negative number: "))
    if num < 0:
        print("Square root is undefined for negative numbers.")
    else:
        sqrt_value = math.sqrt(num)
        print("Square root:", round(sqrt_value, 2))

def sine_and_cosine():
    angle = float(input("Enter an angle in degrees: "))
    angle_in_radians = math.radians(angle)  # converts degrees to radians
    sine_value = math.sin(angle_in_radians)
    cosine_value = math.cos(angle_in_radians)
    print("Sine of the angle:", round(sine_value, 2))
    print("Cosine of the angle:", round(cosine_value, 2))

# Add your solutions to the programming exercises here.
# Remember that the `math` module is already imported for you (do not import it again!)
