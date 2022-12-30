numberOfIterations = int(input())
A = 0
B = 1

if numberOfIterations > 1:
    for i in range(numberOfIterations-1):
        temp = A + B
        A = B
        B = temp

print(str(A) + ' ' + str(B))
