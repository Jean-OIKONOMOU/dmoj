inputComposition = input()
cMajor = 'CFG'
aMinor = 'ADE'
cMajorCount = 0
aMinorCount = 0

for i in range(len(inputComposition)):
    # get the first one
    if i == 0:
        if inputComposition[0] in cMajor:
            cMajorCount += 1
        elif inputComposition[0] in aMinor:
            aMinorCount += 1
    
    if inputComposition[i] == '|':
        if inputComposition[i+1] in cMajor:
            cMajorCount += 1
        elif inputComposition[i+1] in aMinor:
            aMinorCount += 1

if cMajorCount == aMinorCount:
    if inputComposition[len(inputComposition)-1] == 'A':
        print('A-mol')
    else:
        print('C-dur')
elif cMajorCount > aMinorCount:
    print('C-dur')
else:
    print('A-mol')

