moves = input()
position = 1
for move in moves:
    if position == 1:
        if move == "A":
            position = 2
        elif move == "C":
            position = 3
    elif position == 2:
        if move == "A":
            position = 1
        elif move == "B":
            position = 3
    elif position == 3:
        if move == "B":
            position = 2
        elif move == "C":
            position = 1

print(position)
