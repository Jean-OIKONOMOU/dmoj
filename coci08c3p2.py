coded = input()
decoded = ''

i = 0
while i < len(coded):
    decoded = decoded + coded[i]
    if coded[i] in 'aeiou':
        i = i + 3
    else:
        i = i + 1

print(decoded)