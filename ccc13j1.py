youngestSibling = input()
middleSibling = input()

try:
    youngestSibling = int(youngestSibling)
    middleSibling = int(middleSibling)
    if (
        (youngestSibling < 0 or youngestSibling > 50)
        or (youngestSibling > middleSibling)
        or (middleSibling > 50)
    ):
        print("Wrong input")
    else:
        print(middleSibling + (middleSibling - youngestSibling))
except ValueError:
    print("Please enter an integer")
