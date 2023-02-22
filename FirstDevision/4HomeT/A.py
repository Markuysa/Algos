count = int(input())
sinonims = dict()

for i in range(count):
    word,synonim = input().split()
    sinonims[synonim] = word

word = input()

for i, j in sinonims.items():
    if i == word:
        print(j)
    elif j == word:
        print(i)
