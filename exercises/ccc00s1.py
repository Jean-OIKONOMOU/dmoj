quarters    = int(input())
playedOne   = int(input())
playedTwo   = int(input())
playedThree = int(input())

totalPlayed = 0
machine = 0

while(quarters >= 1):

    # make it play just one slot machine per iteration
    if totalPlayed%3 == 0:
        if(playedOne%35 == 0):
            quarters += 30
    elif totalPlayed%3 == 1:
        if(playedTwo%100 == 0):
            quarters += 60
    elif totalPlayed%3 == 2:
        if(playedThree%10 == 0):
            quarters += 9
    
    quarters -= 1
    totalPlayed += 1

        
print('Martha plays '+ str(totalPlayed) +' times before going broke.')



