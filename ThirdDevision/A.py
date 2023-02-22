f = open("input.txt")
entries = dict()

for line in f.readlines():
    for char in line:
        if char != ' ' and char != '\n':
            if char not in entries:
                entries[char] = 1
            entries[char] += 1


line = sorted(entries.keys(),reverse=False)
maxValue = max(entries.values())
while maxValue != 1:
    temp = []
    for i in line:
        if entries[i] >= maxValue:
            temp.append('#')
        else:
            temp.append(' ')
    maxValue -= 1
    print(''.join(temp))
print(''.join(line))
