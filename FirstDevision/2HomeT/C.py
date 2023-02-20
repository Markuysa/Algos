`
size = int(input())

mas = list(map(int,input().split()))

x = int(input())

if len(mas)>0:
    number = mas[0]
    minDiff = abs(number - x)
    for i in mas:
        if abs(x - i) < minDiff:
            minDiff = abs(x - i)
            number = i

    print(number)`