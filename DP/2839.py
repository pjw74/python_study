# 설탕 배달:
# https://www.acmicpc.net/problem/2839
import sys

input = sys.stdin.readline
answer = 0
N = int(input())

while N > 0:
    if N % 5 != 0:
        N -= 3
        answer += 1
    else:
        answer += N // 5
        N = N % 5
if N < 0:
    answer = -1



print(answer)
