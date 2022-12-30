villages = int(input())
nbs = []
nbsSize = 0

for i in range(villages):
    nbs.append(int(input()))

nbs.sort()
print(nbs)
nbsSize = (nbs[1] - nbs[0])/2 + (nbs[2] - nbs[1])/2

for j in range(1, len(nbs)-1):
    if nbsSize > (nbs[j] - nbs[j-1])/2 + (nbs[j+1] - nbs[j])/2:
        nbsSize = (nbs[j] - nbs[j-1])/2 + (nbs[j+1] - nbs[j])/2

print(nbsSize)