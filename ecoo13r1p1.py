lines = int(input())

act = ''

takeCounter = 0
serveCounter = 0
counter = lines

while act != 'EOF':
    act = input()
    if counter == 999:
        counter = 0

    if takeCounter == 999:
        takeCounter = 0

    if act == 'TAKE':
        takeCounter = takeCounter + 1
        counter = counter + 1

    if act == 'SERVE':
        serveCounter = serveCounter + 1
    
    if act == 'CLOSE':
        print(f'{takeCounter} {takeCounter-serveCounter} {counter}')
        takeCounter = 0
        serveCounter = 0