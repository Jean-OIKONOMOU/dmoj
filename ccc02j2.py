inputWord = ''
while inputWord != 'quit!':
    inputWord = input()
    if len(inputWord) >= 4 and inputWord[-2:] == 'or' and inputWord[-3:-2] not in 'aeiouy':
        print(inputWord[:-1]+'ur')
    elif inputWord != 'quit!':
        print(inputWord)