import sys
from collections import deque

M, N, K = map(int, input().split())
# graph = [[list(map(int, input().rstrip()))]]
graph = [[0] * N for _ in range(M)]
dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]
cnt = []
for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            graph[j][k] = 1
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            count = 1
            graph[i][j] = 1
            queue = deque()
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    x1 = x + dr[k]
                    y1 = y + dc[k]
                    if 0 <= x1 < M and 0 <= y1 < N and graph[x1][y1] == 0:
                        graph[x1][y1] = 1
                        count += 1
                        queue.append([x1, y1])
            cnt.append(count)
print(len(cnt))
cnt.sort()
for i in cnt:
    print(i, end=" ")
