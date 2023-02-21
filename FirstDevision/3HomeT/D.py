import re

resultSet = set()
file = open("input.txt")

for line in file.readlines():
    resultSet.update(set(re.split(r"\s+", line)))
resultSet.remove("")
print(len(resultSet))
