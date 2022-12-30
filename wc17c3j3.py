possiblePassword = input()

lowercaseCount = 0
uppercaseCount = 0
digitCount = 0

if 8 <= len(possiblePassword) and 12 >= len(possiblePassword):
    for letters in possiblePassword:
        if letters.isupper() and letters.isnumeric() == False:
            uppercaseCount += 1
        elif letters.isupper() == False and letters.isnumeric() == False:
            lowercaseCount += 1
        else:
            digitCount += 1
    
    if lowercaseCount >= 3 and uppercaseCount >= 2 and digitCount >= 1:
        print('Valid')
    else:
        print('Invalid')

else:
    print('Invalid')