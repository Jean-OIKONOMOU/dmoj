monthlyMegabytes = int(input())
months = int(input())

res = 0

for month in range(months):
    monthlyMegabytesUsed = int(input())
    res = monthlyMegabytes + res - monthlyMegabytesUsed 

print(res+monthlyMegabytes)