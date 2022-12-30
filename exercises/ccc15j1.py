month = input()
day = input()

try:
    month = int(month)
    day = int(day)
    if month > 2:
        print("After")
    elif month < 2:
        print("Before")
    elif month == 2:
        if day == 18:
            print("Special")
        elif day > 18:
            print("After")
        else:
            print("Before")
except ValueError:
    print("Please enter an integer")
