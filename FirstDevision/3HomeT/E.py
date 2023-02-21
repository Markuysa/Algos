buttonsSet = set(input().split())

number = input()

counter = 0

checkedNumbers = set()
for i in number:
    if not (i in buttonsSet) and not (i in checkedNumbers):
        counter += 1
        checkedNumbers.add(i)
print(counter)
