# # # Halftime lasts from 0s to 1440s inclusive.
# # # A whole match is 2880s, not inclusive, or 4*12m.

# # # 1. How many points have been scored during the first half-time ?
# # # 2. How many turnarounds are there ? 

halftime = 1440
inputLinesA = int(input())
teamATimestamps = []

for _ in range(inputLinesA):
    timestampsA = int(input())
    teamATimestamps.append(timestampsA)

inputLinesB = int(input())
teamBTimestamps = []

for _ in range(inputLinesB):
    timestampsB = int(input())
    teamBTimestamps.append(timestampsB)

# Question 1
halfTimePoints = 0

for i in teamATimestamps:
    if i <= halftime:
        halfTimePoints = halfTimePoints + 1

for i in teamBTimestamps:
    if i <= halftime:
        halfTimePoints = halfTimePoints + 1

# Question 2
# sort timestamps
goalsA = 0
goalsB = 0
turnaround = 0
goalList = []
turnA = True
turnB = True

for i in range(2880):
    if i in teamATimestamps:
        goalsA = goalsA +1
        if goalsB != 0 and goalsA > goalsB and turnA:
            turnaround = turnaround +1
            turnA = False
            turnB = True
    
    if i in teamBTimestamps:
        goalsB = goalsB +1
        if goalsA != 0 and goalsB > goalsA and turnB:
            turnaround = turnaround +1    
            turnA = True
            turnB = False    

print(halfTimePoints)
print(turnaround)
