yearOnePrice = 12
yearTwoPrice = 10
yearThreePrice = 7
yearFourPrice = 5

for _ in range(10):
    # first line is the cost of the trip
    tripCost = int(input()) 
    
    # four decimal numbers 0<x<1 representing percentages, put in a string and each separated by a space
    studentPercentages = input().split() 
    for i in range (0,len(studentPercentages)):
        studentPercentages[i] = float(studentPercentages[i])

    # total students coming for the brunch
    attendingStudents = int(input()) 

    # pre calculating student numbers based on the percentages
    yearOneStudents   = int(attendingStudents*studentPercentages[0])
    yearTwoStudents   = int(attendingStudents*studentPercentages[1])
    yearThreeStudents = int(attendingStudents*studentPercentages[2])
    yearFourStudents  = int(attendingStudents*studentPercentages[3])

    studentArrPrcnt = [yearOneStudents, yearTwoStudents, yearThreeStudents, yearFourStudents]

    # total number of students 
    studentYearPrcnt = sum(studentArrPrcnt)

    # si ce nombre est different du nombre total d'étudiant qui nous est donné alors ajouter la différence (positive ou négative) au pourcentage le plus grand d'étudiants
    if studentYearPrcnt != attendingStudents:
        # should I add or remove students ?
        studentsToAdd = attendingStudents - studentYearPrcnt
        # which year has the most students ?
        biggestPercent = studentPercentages[0]
        biggestPercentYear = 0
        for i in range(1,len(studentPercentages)):
            if studentPercentages[i] > biggestPercent:
                biggestPercent = studentPercentages[i]
                biggestPercentYear = i
        # Doing the calculus. Doing an addition is always good whether I want to remove, or add, students.
        studentArrPrcnt[biggestPercentYear] = studentArrPrcnt[biggestPercentYear] + studentsToAdd
        # new total number of students 
        studentYearPrcnt = sum(studentArrPrcnt)

    # calculate the money we'll win
    yearOneMoney   = studentArrPrcnt[0]*yearOnePrice
    yearTwoMoney   = studentArrPrcnt[1]*yearTwoPrice
    yearThreeMoney = studentArrPrcnt[2]*yearThreePrice
    yearFourMoney  = studentArrPrcnt[3]*yearFourPrice

    totalMoney = yearOneMoney + yearTwoMoney + yearThreeMoney + yearFourMoney

    if int(totalMoney)*0.5 < tripCost:
        print('YES')
    else:
        print('NO')
