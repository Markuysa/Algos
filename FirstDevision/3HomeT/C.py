anya, borya = map(int, input().split())

anyaSet = set()
boryaSet = set()

for i in range(anya):
    anyaSet.add(int(input()))
for i in range(borya):
    boryaSet.add(int(input()))
intersec = sorted(anyaSet.intersection(boryaSet))
aintersec = sorted(anyaSet.difference(intersec))
bintersec = sorted(boryaSet.difference(intersec))

print(len(intersec))
print(" ".join(map(str, intersec)))

print(len(aintersec))
print(" ".join(map(str, aintersec)))

print(len(bintersec))
print(" ".join(map(str, bintersec)))
