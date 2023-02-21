numbers = []
number = int(input())
while number != -2000000000:
    numbers.append(number)
    number = int(input())

solutions = [False for i in range(7)]
if len(numbers) > 0:
    flag = False
    i = 0
    first = numbers[0]
    while first == numbers[i]:
        first = numbers[i]
        i += 1
        if first == numbers[-1]:
            print("CONSTANT")
            flag = True
            break
    i = 0
    first = numbers[0]
    if not flag:
        while True:
            if first <= numbers[i]:
                break
            first = numbers[i]
            i += 1
            if i == len(numbers):
                print("ASCENDING")
                flag = True
                break
    i = 0
    first = numbers[0]
    if not flag:
        while True:
            if first >= numbers[i]:
                break
            first = numbers[i]
            i += 1
            if i == len(numbers):
                print("DESCENDING")
                flag = True
                break
    i = 0
    first = numbers[0]
    if not flag:
        while True:
            if first > numbers[i]:
                break
            first = numbers[i]
            i += 1
            if i == len(numbers):
                print("WEAKLY ASCENDING")
                flag = True
                break
    i = 0
    first = numbers[0]
    if not flag:
        while True:
            if first < numbers[i]:
                break
            first = numbers[i]
            i += 1
            if i == len(numbers):
                print("WEAKLY DESCENDING")
                flag = True
                break
    if not flag:
        print("RANDOM")
