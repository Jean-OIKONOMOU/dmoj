questions = int(input())
answers   = input()

i = 0

adrianSequence = 'ABC'
brunoSequence  = 'BABC'
goranSequence  = 'CCAABB'

adrianScore = 0
brunoScore  = 0
goranScore  = 0

while i < questions:
    if answers[i%len(answers)] == adrianSequence[i%3]:
        adrianScore = adrianScore + 1
    if answers[i%len(answers)] == brunoSequence[i%4]:
        brunoScore = brunoScore + 1
    if answers[i%len(answers)] == goranSequence[i%6]:
        goranScore = goranScore + 1
    i = i + 1

# adrian bruno goran
if (adrianScore == brunoScore) and (adrianScore == goranScore):
    print(adrianScore)
    print('Adrian')
    print('Bruno')
    print('Goran')
# adrian bruno
if (adrianScore == brunoScore) and (brunoScore > goranScore):
    print(adrianScore)
    print('Adrian')
    print('Bruno')
# adrian goran
if (adrianScore == goranScore) and (goranScore > brunoScore):
    print(adrianScore)
    print('Adrian')
    print('Goran')
# bruno goran
if (brunoScore == goranScore) and (goranScore > adrianScore):
    print(brunoScore)
    print('Bruno')
    print('Goran')
# adrian
if (adrianScore > brunoScore) and (adrianScore > goranScore):
    print(adrianScore)
    print('Adrian')
# bruno
if (brunoScore > goranScore) and (brunoScore > adrianScore):
    print(brunoScore)
    print('Bruno')
# goran
if (goranScore > brunoScore) and (goranScore > adrianScore):
    print(goranScore)
    print('Goran')

