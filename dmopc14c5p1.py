from cmath import pi
from xml.etree.ElementTree import PI

# Import math Library
import math

radius = input()
height = input()

try:
    radius = int(radius)
    height = int(height)
    if (radius < 1 or radius > 100) or (height < 1 or height > 100):
        print("Wrong input")
    else:
        print((math.pi * (radius**2) * height) / 3)
except ValueError:
    # Handle the exception
    print("Please enter an integer")
