import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    temp = []
    temp.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nc = x + dc[i]
            nr = y + dr[i]
            if 0 <= nc < N and 0 <= nr < N and visited[nc][nr] == 0:
                # 국경선을 공유하는 두 나라의 인구 차이가 L이상,R이하라면 국경선 공유
                if L <= abs(graph[nc][nr] - graph[x][y]) <= R:
                    visited[nc][nr] = 1
                    queue.append((nc, nr))
                    temp.append((nc, nr))
    return temp


result = 0
while 1:
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)
                # 위의 조건에 의해 인구이동을 시작
                if len(country) > 1:
                    flag = 1
                    number = sum([graph[x][y] for x, y in country]) // len(country)
                    for x, y in country:
                        graph[x][y] = number
    if flag == 0:
        break
    result += 1

print(result)
