C = input()

try:
    C = int(C)

    if C < -40 or C > 40:
        print("Wrong input")
    else:
        print(((C * (9 / 5)) + 32))
except ValueError:
    print("Please enter an integer")
