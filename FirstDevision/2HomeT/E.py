smans = int(input())
goals = list(map(int, input().split()))

maxGoal = max(goals)
place = 0
resPlace = 0
t_goal = 0
winnerThrowed = False
for i in range(len(goals) - 1):
    if goals[i] == maxGoal and not winnerThrowed:
        winnerThrowed = True
    elif winnerThrowed and goals[i] % 10 == 5 and goals[i + 1] < goals[i]:
        if goals[i] > t_goal:
            t_goal = goals[i]
            place = i
if place != 0:
    goal = goals[place]
    for i in range(len(goals)):
        if goals[i] > goal:
            resPlace += 1
    resPlace += 1
print(resPlace)

