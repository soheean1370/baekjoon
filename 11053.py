import sys
input = sys.stdin.readline

a = int(input())
lst_a = list(map(int, input().split()))

dp = [1] * a

for i in range(1, a):
    for j in range(i):
        if lst_a[i] > lst_a[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))