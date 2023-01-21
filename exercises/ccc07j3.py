# Variable declarations
dollarAmounts = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
i = 0

# Main
openedCases = int(input()) 

for _ in range(openedCases):
  eliminatedCasePos = int(input())-1
  dollarAmounts[eliminatedCasePos] = 0
  i = i + 1

bankerOffer = int(input())
average = round(sum(dollarAmounts) / (len(dollarAmounts) - openedCases))

if bankerOffer > average:
    print('deal')
else:
    print('no deal')
