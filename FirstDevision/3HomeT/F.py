
firstGenom = input()
secondGenom = input()

firstTuple = tuple(firstGenom[i:i+2] for i in range(len(firstGenom) - 1))
secondSet = set(secondGenom[i:i+2] for i in range(len(secondGenom) - 1))
resultCounter = 0

for i in firstTuple:
    if i in secondSet:
        resultCounter+=1

print(resultCounter)
