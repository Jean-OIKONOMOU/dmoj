handSize = int(input())
hand = []
deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]

# create hand
for i in range(handSize):
    card = int(input())
    hand.append(card)

# remove drawn cards from the deck
for j in hand:
    if j in deck:
        deck.remove(j)

# calculate the blackjack number
x = 21 - sum(hand)

# calculate how many cards are higher, or lower, than X

cardsGreaterThanX = 0
cardsSmallerThanX = 0

for k in deck:
    if k > x:
        cardsGreaterThanX = cardsGreaterThanX + 1
    else:
        cardsSmallerThanX = cardsSmallerThanX + 1

if cardsGreaterThanX >= cardsSmallerThanX:
    print('DOSTA')
else:
    print('VUCI')