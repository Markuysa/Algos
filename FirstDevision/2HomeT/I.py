# Вам необходимо построить поле для игры "Сапер" по его конфигурации – размерам и координатам расставленных на нем мин.

# Вкратце напомним правила построения поля для игры "Сапер":
# Поле состоит из клеток с минами и пустых клеток
# Клетки с миной обозначаются символом *
# Пустые клетки содержат число ki,j, 0≤ ki, j ≤ 8 – количество мин на соседних клетках.
# Соседними клетками являются восемь клеток, имеющих смежный угол или сторону.
# UNFINISHED
rows, columns, mines = map(int, input().split())
minescoord = {}
playground = [[0] * columns for i in range(rows)]


def printplayground(playground):
    for i in playground:
        for j in range(len(i)):
            if j == len(i) - 1:
                print(str(i[j]))
            else:
                print(str(i[j]) + " ", end="")


for _ in range(mines):
    row, column = map(int, input().split())
    row, column = row - 1, column - 1
    minescoord[row] = column
    playground[row][column] = "*"
printplayground(playground)
