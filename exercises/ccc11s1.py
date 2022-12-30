numberOfSentences = int(input())
completeString = ''

for i in range(numberOfSentences):
    inputString = input()
    completeString += inputString

tCount = 0
sCount = 0

for letter in completeString:
    if letter == 't' or letter == 'T':
        tCount += 1
    elif letter == 's' or letter == 'S':
        sCount += 1

if tCount > sCount:
    print('English')
else:
    print('French')