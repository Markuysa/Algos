
stickersNumber = int(input())

stickers = list(map(int,input().split()))

collectorsNumber = int(input())

collectorsStickers = map(int,input().split())

results = [0]*collectorsNumber

currentCollector = 0
for collectorsSticker in collectorsStickers:
    checkedStickers = set()
    for sticker in stickers:
        if collectorsSticker > sticker and sticker not in checkedStickers:
            results[currentCollector] += 1
            checkedStickers.add(sticker)
    currentCollector += 1

for result in results:
    print(result)

