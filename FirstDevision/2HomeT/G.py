# Дан список, заполненный произвольными целыми числами.
# Найдите в этом списке два числа, произведение которых максимально.
# Выведите эти числа в порядке неубывания.
# Список содержит не менее двух элементов. Числа подобраны так, что ответ однозначен.

numbers = list(map(int, input().split()))

first = numbers[0]
maxMult = 0
maxF = max(numbers)
index = numbers.index(maxF)
newmas = numbers[:index] + numbers[index + 1 :]
maxS = max(newmas)

minF = min(numbers)
index = numbers.index(minF)
newmas = numbers[:index] + numbers[index + 1 :]
minS = min(newmas)


if maxF * maxS > minF * minS:
    print(min(maxF, maxS), max(maxF, maxS))
else:
    print(min(minF, minS), max(minF, minS))
