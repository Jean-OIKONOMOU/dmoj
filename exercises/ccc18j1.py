from ast import Try


firstNum = input()
secondNum = input()
thirdNum = input()
fourthNum = input()

try:
    firstNum = int(firstNum)
    secondNum = int(secondNum)
    thirdNum = int(thirdNum)
    fourthNum = int(fourthNum)

    if (
        (0 <= firstNum < 10)
        and (0 <= secondNum < 10)
        and (0 <= thirdNum < 10)
        and (0 <= fourthNum < 10)
    ):
        if (
            (firstNum == 8 or firstNum == 9)
            and (secondNum == thirdNum)
            and (fourthNum == 8 or fourthNum == 9)
        ):
            print("ignore")
        else:
            print("answer")
    else:
        print("Invalid number.")
except ValueError:
    print("Please enter an integer")
