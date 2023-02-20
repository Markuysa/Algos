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


def sol(a, n):
    max_a = max(a)
    t_dist = 0  # столько точно не выбил
    to_find = False

    for i in range(n - 1):
        if a[i] == max_a and not to_find:
            to_find = True
        elif to_find:
            a2 = a[i]
            a3 = a[i + 1]
            if (a2 % 10) == 5 and a2 > a3:
                if a2 > t_dist:
                    t_dist = a2
    print(t_dist)
    if t_dist:  # найден в списке
        t_pos = 1
        for dist in a:
            if dist > t_dist:
                t_pos += 1
        return t_pos
    else:
        return 0


n = int(input())
a = list(map(int, input().split()))

print(sol(a, n))
