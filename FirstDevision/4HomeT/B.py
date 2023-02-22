import re

file = open("input.txt")
result = []
dic = dict()
for line in file.readlines():
    if line == '\n' or line == "":
        continue
    words = re.split(r"\s+", line)
    for word in words:
        if word=='\n' or word=='':
            continue
        if word not in dic.keys() and word!='\n':
            dic[word] = 0
            result .append(str(0) + " ")
        else:
            dic[word] += 1
            result.append(str(dic[word]) + " ")
print(''.join(result))
