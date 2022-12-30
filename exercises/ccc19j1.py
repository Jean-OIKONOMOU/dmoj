apples3 = input()
apples2 = input()
apples1 = input()
banana3 = input()
banana2 = input()
banana1 = input()

try:
    apples3 = int(apples3)
    apples2 = int(apples2)
    apples1 = int(apples1)
    banana3 = int(banana3)
    banana2 = int(banana2)
    banana1 = int(banana1)

    applesTotalScore = (apples3 * 3) + (apples2 * 2) + apples1
    bananasTotalScore = (banana3 * 3) + (banana2 * 2) + banana1

    if applesTotalScore > bananasTotalScore:
        print("A")
    elif applesTotalScore < bananasTotalScore:
        print("B")
    else:
        print("T")
except ValueError:
    print("Please enter an integer")
