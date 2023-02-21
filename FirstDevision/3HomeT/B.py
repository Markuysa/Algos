firstSet = set(map(int, input().split()))
secondSet = set(map(int, input().split()))

result = sorted(firstSet.intersection(secondSet))

print(" ".join(map(str, result)))
