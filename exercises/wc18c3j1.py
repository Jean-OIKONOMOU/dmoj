litresOfPaint = input()
paintPerCap = input()
capPrice = input()

try:
    litresOfPaint = int(litresOfPaint)
    paintPerCap = int(paintPerCap)
    capPrice = int(capPrice)
    if (
        (1 <= litresOfPaint <= 100)
        and (1 <= paintPerCap <= 100)
        and (1 <= capPrice <= 100)
    ):
        numberOfCaps = litresOfPaint // paintPerCap
        capBenefits = numberOfCaps * capPrice
        leftoverPaint = litresOfPaint % paintPerCap
        print((capBenefits + leftoverPaint))
    else:
        print("Wrong input")
except ValueError:
    print("Please enter an integer")
