# # # Halftime lasts from 0s to 1440s inclusive.
# # # A whole match is 2880s, not inclusive, or 4*12m.

# # # 1. How many points have been scored during the first half-time ?
# # # 2. How many turnarounds are there ? 

# halftime = 1440
# inputLinesA = int(input())
# teamATimestamps = []

# timestampsA = [0, 'A']
# for _ in range(inputLinesA):
#     timestampsA[0] = int(input())
#     teamATimestamps.append(timestampsA)

# inputLinesB = int(input())
# teamBTimestamps = []

# timestampsB = [0, 'B']
# for _ in range(inputLinesB):
#     timestampsB[0] = int(input())
#     teamBTimestamps.append(timestampsB)

# # Question 1
# halfTimePoints = 0

# for i in teamATimestamps:
#     if i <= halftime:
#         halfTimePoints = halfTimePoints + 1

# for i in teamBTimestamps:
#     if i <= halftime:
#         halfTimePoints = halfTimePoints + 1
teamATimestamps = [10, 1400, 1500]
teamBTimestamps = [7, 2000]
# Question 2
# sort timestamps
# for i in range(0,len(arr2)):
#     for j in range(i+1,len(arr2)):
#         if arr2[i] > arr2[j]:
#             temp = arr2[i]
#             arr2[i] = arr2[j]
#             arr2[j] = temp
# print(arr2)
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

print(turnaround)

# for j in teamATimestamps:
#     goalList.append(['A', j])

# print(goalList)

# goalList = teamATimestamps + teamBTimestamps
# goalList.sort()
# print(goalList)



# # print(halfTimePoints)

# for i in range(0,len(arr2)):
#     for j in range(i+1,len(arr2)):
#         if arr2[i] > arr2[j]:
#             temp = arr2[i]
#             arr2[i] = arr2[j]
#             arr2[j] = temp
# print(arr2)


# # # Halftime lasts from 0s to 1440s inclusive.
# # # A whole match is 2880s, not inclusive, or 4*12m.

# # # 1. How many points have been scored during the first half-time ?
# # # 2. How many turnarounds are there ? 

halftime = 1440
inputLinesA = int(input())
teamATimestamps = []

timestampsA = [0, 'A']
for _ in range(inputLinesA):
    timestampsA[0] = int(input())
    teamATimestamps.append(timestampsA)

inputLinesB = int(input())
teamBTimestamps = []

timestampsB = [0, 'B']
for _ in range(inputLinesB):
    timestampsB[0] = int(input())
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

