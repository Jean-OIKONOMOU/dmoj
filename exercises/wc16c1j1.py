spooks = input()

try:
    spooks = int(spooks)
    if 2 > spooks or spooks > 20:
        print("Wrong input")
    else:
        print("sp" + ("o" * spooks) + "ky")
except ValueError:
    print("Please enter an integer")
