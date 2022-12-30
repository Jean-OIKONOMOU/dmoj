elderWandWizard = input()
wizardBattles = int(input())
wizardCounter = 1

for battles in range(wizardBattles):
    battleContestants = input()
    if elderWandWizard == battleContestants[2]:
        elderWandWizard = battleContestants[0]
        wizardCounter = wizardCounter + 1

print(elderWandWizard)
print(wizardCounter)