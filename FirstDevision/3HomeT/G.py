
N = int(input())
pairs = set()

counter = 0
for _ in range(N):
    a,b = map(int,input().split())
    if a + b == N - 1 and a >= 0 and b >= 0:
        pairs.add((a,b))
print(len(pairs))
