bowl1 = int(input())
bowl2 = int(input())
bowl3 = int(input())

if bowl1 > bowl2:
    if bowl1 < bowl3:
        print(bowl1)
    elif bowl2 > bowl3:
        print(bowl2)
    else:
        print(bowl3)
else:
    if bowl1 > bowl3:
        print(bowl1)
    elif bowl2 < bowl3:
        print(bowl2)
    else:
        print(bowl3)
