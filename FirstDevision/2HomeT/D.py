
numbers = list(map(int,input().split()))

counter = 0
for i in range(1,len(numbers)):
    if i == len(numbers) - 1:
        break
    elif numbers[i] > numbers[i+1] and numbers[i] > numbers[i-1]:
        counter+=1
print(counter)