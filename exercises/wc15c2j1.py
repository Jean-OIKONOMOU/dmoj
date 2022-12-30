fars = input()

try:
    fars = int(fars)
    if 1 > fars or fars > 5:
        print("Wrong input")
    else:
        print("A long time ago in a galaxy " + ("far, " * (fars - 1)) + "far away...")
except ValueError:
    print("Please enter an integer")
