elderWandWizard = input()
rows = int(input()) 
ownerCounter = 1
wizardBattleDataset = []
wizardOwners = [elderWandWizard]

for row in range(rows):
    battleContestants = input().split()
    wizardBattleDataset.append(battleContestants)

for row in range(rows):
    if wizardBattleDataset[row][1] == elderWandWizard:
        elderWandWizard = wizardBattleDataset[row][0]
        # is that owner already in the list though ?
        if elderWandWizard not in wizardOwners: 
            ownerCounter = ownerCounter + 1
        wizardOwners.append(elderWandWizard)

print(wizardOwners[len(wizardOwners)-1])
print(ownerCounter)