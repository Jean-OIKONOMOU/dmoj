for dataset in range(10):
    F_D = input().split()
    columns = int(F_D[0])
    rows = int(F_D[1])
    dataTable = []
    
    for row in range(rows):
        temp = input().split()
        for column in range(columns):
            temp[column] = int(temp[column])
        dataTable.append(temp)

    bonuses = 0

    for row in dataTable:
        total = sum(row)
        if total % 13 == 0:
            bonuses = bonuses + total//13

    for column in range(columns):
        total = 0
        for row in range(rows):
            total = total + dataTable[row][column]
        if total%13==0:
            bonuses = bonuses + total//13
    
    print(bonuses)

