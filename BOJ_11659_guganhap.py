import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

dp = [0]
sum_a = 0
for k in lst:
    sum_a += k
    dp.append(sum_a)

for n in range(M):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])