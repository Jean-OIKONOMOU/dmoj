color = ''
timer = 0
redCounter = 0
nonredCounter = 0


while color != 'end of box':
    color = input()

    if color in 'orangebluegreenyellowpinkvioletbrown':
        nonredCounter = nonredCounter + 1
    elif color == 'red':
        redCounter = redCounter + 1

print(f'{nonredCounter} {redCounter}')

print(f'{int(nonredCounter/7)*13} {(redCounter*16)}')

timer += int(nonredCounter/7)*13 + (redCounter*16)

if nonredCounter%7 != 0:
    timer = timer + 13

print(timer)
