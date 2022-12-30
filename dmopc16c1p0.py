width = input()
cheese = input()

try:
    width = int(width)
    cheese = int(cheese)
    if width == 3 and cheese >= 95:
        print("C.C. is absolutely satisfied with her pizza.")
    elif width == 1 and cheese <= 50:
        print("C.C. is fairly sastisfied with her pizza.")
    else:
        print("C.C. is very satisfied with her pizza.")
except ValueError:
    print("Please enter an integer")
