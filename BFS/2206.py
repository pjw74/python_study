# https://www.acmicpc.net/problem/2206

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
# 3차원 행렬을 통해 벽의 파괴를 파악. visited[x][y][0]은 벽 파괴 가능, [x][y][1]은 불가능
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1


def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()
        # 끝 점에 도달하면 이동 횟수 출력
        if a == N - 1 and b == M - 1:
            return visited[a][b][c]
        for i in range(4):
            dc = [-1, 1, 0, 0]
            dr = [0, 0, -1, 1]

            nc = a + dc[i]
            nr = b + dr[i]
            if nc < 0 or nc >= N or nr < 0 or nr >= M:
                continue
            # 다음 이동할 곳이 벽이고, 벽 파괴 기회를 사용하지 않은 경우
            if graph[nc][nr] == 1 and c == 0:
                visited[nc][nr][1] = visited[a][b][0] + 1
                queue.append((nc, nr, 1))
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
            elif graph[nc][nr] == 0 and visited[nc][nr][c] == 0:
                visited[nc][nr][c] = visited[a][b][c] + 1
                queue.append((nc, nr, c))
    return -1


print(bfs(0, 0, 0))
