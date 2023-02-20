# doesn't work hz why __)_)_
# TODO FIX this shit with FD B task
numbers= []
while True:
    number = int(input())
    if number == -2 * 10**9:
        break
    numbers.append(number)
solutions = [False for i in range(7)]
if len(numbers) > 0:
    flag = False
    i = 0
    first = numbers[0]
    while first == numbers[i]:
        first = numbers[i]
        if first == numbers[-1]:
            print("CONSTANT")
            flag = True
            break
    first = numbers[0]
    if not flag:
        while first < numbers[i]:
            first = numbers[i]
            if first == numbers[-1]:
                print("ASCENDING")
                flag = True
                break
    if not flag:
        while first > numbers[i]:
            first = numbers[i]
            if first == numbers[-1]:
                print("DESCENDING")
                flag = True
                break
    if not flag:
        while first <= numbers[i]:
            first = numbers[i]
            if first == numbers[-1]:
                print("WEAKLY ASCENDING")
                flag = True
                break
    if not flag:
        while first >= numbers[i]:
            first = numbers[i]
            if first == numbers[-1]:
                print("WEAKLY DESCENDING")
                flag = True
                break
    if not flag:
        print("RANDOM")


