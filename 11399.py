import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(map(int, input().split()))

dp = [0] * (n+1)
dp[0] = lst[0]

for i in range(1,n):
    dp[i] = lst[i] + dp[i-1]

print(sum(dp))
