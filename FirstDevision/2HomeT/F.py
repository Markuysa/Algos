# TODO FINISH
def checkSymmetry(line):
    flag = True
    middle = len(line) // 2
    i = 1
    if len(line) % 2 == 0:
        while middle < len(line):
            if line[middle] == line[middle - i]:
                middle += 1
                i += 2
            else:
                flag = False
                break
    else:
        left = middle - 1
        right = middle + 1
        while left >= 0 and right < len(line):
            if line[left] == line[right]:
                left -= 1
                right += 1
            else:
                flag = False
                break
    return flag


size = int(input())

numbers = list(map(int, input().split()))


numberscount = 0
addLine = ""
indexes = ()
flag = False
if not checkSymmetry(numbers):
    left = len(numbers) - 2
    right = len(numbers) - 1
    while right < len(numbers):
        if numbers[left] == numbers[right]:
            left -= 1
            right -= 1
            flag = True
        else:
            left += 1
            right += 1
    print(left, right)


print(numberscount)
print(addLine)
