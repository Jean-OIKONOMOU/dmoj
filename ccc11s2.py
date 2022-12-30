numberOfquestions = int(input())
answersString = ''
solutionsString = ''

for i in range(numberOfquestions):
    answerString = input()
    answersString += answerString

for i in range(numberOfquestions):
    solutionString = input()
    solutionsString += solutionString

correctAnswersCount = 0

for i in range(numberOfquestions):
    if answersString[i] == solutionsString[i]:
        correctAnswersCount += 1

print(correctAnswersCount)