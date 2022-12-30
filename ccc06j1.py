burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

burgerArr = [0, 461, 431, 420, 0]
sideArr = [0, 100, 57, 70, 0]
drinkArr = [0, 130, 160, 118, 0]
dessertArr = [0, 167, 266, 75, 0]
print(
    "Your total Calorie count is "
    + str(burgerArr[burger] + sideArr[side] + drinkArr[drink] + dessertArr[dessert])
    + "."
)
