lines = int(input())
counter = 0
symbol = ''
output = ''

for i in range(lines):
    word = input()
    counter = 0
    output  = ''

    symbol = word[0]
    for j in range(len(word)):
        
        if symbol == word[j]: 
            counter = counter + 1
        
        if symbol != word[j]: 
            output = output + str(counter) + ' ' + symbol + ' '
            counter = 1
            symbol = word[j]
        
        if j+1 == len(word):
            output = output + str(counter) + ' ' + symbol + ' '
        
    print(output)
