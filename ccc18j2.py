N = input()
parkingToday = input()
parkingYesterday = input()
res = 0
for spots in range(int(N)):
    if parkingToday[spots] == 'C':
        if parkingToday[spots] == parkingYesterday[spots]:
            res += 1

print(res)