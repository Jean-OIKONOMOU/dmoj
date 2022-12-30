honiString = input()

honiBlock = ''
honiBlocks = 0

for letter in honiString:
    if len(honiBlock) == 0 and letter == 'H':
        honiBlock = 'H'
    
    if len(honiBlock) == 1 and letter == 'O':
        honiBlock = 'HO'

    if len(honiBlock) == 2 and letter == 'N':
        honiBlock = 'HON'
    
    if len(honiBlock) == 3 and letter == 'I':
        honiBlocks += 1
        honiBlock = ''


print(honiBlocks)