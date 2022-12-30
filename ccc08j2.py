pressedButton = 0

playlist = "ABCDE" 

while pressedButton != 4:
    pressedButton   = int(input())
    numberOfPresses = int(input())
    
    for x in range(numberOfPresses):
        if pressedButton == 1:
            playlist = playlist[1:] + playlist[0]
        elif pressedButton == 2:
            playlist = playlist[-1] + playlist[:-1]
        elif pressedButton == 3:
            playlist = playlist[1] + playlist[0] + playlist[2:]

playlistWithSpaces = ''

for x in range(len(playlist)):
    playlistWithSpaces = playlistWithSpaces + ' ' + playlist[x]

print(playlistWithSpaces)

# pressedButton = 0

# playlist = "A, B, C, D, E"

# while pressedButton != 4:
#     pressedButton   = int(input())
#     numberOfPresses = int(input())
    
#     for x in range(numberOfPresses):
#         if pressedButton == 1:
#             playlist = playlist + ', ' + playlist[0:1]
#             playlist = playlist[3:len(playlist)]
#         elif pressedButton == 2:
#             playlist = playlist[len(playlist)-1:len(playlist)] + ', ' + playlist
#             playlist = playlist[0:len(playlist)-3]
#         elif pressedButton == 3:
#             playlist = playlist[3:4] + ', ' + playlist[0:1] + playlist[4:len(playlist)]

# print(playlist.replace(',', ''))
