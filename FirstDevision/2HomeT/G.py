
numbers = list(map(int,input().split()))

maxMult = 0
if len(numbers) > 3:
    maxF = max(numbers)
    index = numbers.index(maxF)
    newmas = numbers[:index] + numbers[index + 1:]

    maxS = max(newmas)
    index = newmas.index(maxS)
    newmas= newmas[:index] + newmas[index + 1:]

    maxT = max(newmas)

    minF = min(newmas)
    index = newmas.index(minF)
    newmas= newmas[:index] + newmas[index + 1:]

    minS = min(newmas)
    index = newmas.index(minS)
    newmas= newmas[:index] + newmas[index + 1:]

    if minS*minF* maxF > maxF*maxS*maxT:
        print(maxF, max(minS,minF),min(minS,minF))
    else:
        print(maxF, maxS, maxT)
else:
    print(numbers[0],numbers[1],numbers[2])