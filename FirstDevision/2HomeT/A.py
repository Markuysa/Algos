

mas = list(map(int,input().split()))
prev = mas[0]
flag = True
for i in mas:
    if i < prev:
        flag = False
        break
    else:
        prev = i
if flag:
    print("YES")
else:
    print("NO")
