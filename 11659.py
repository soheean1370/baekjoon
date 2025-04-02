import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))


prefix_sum = [0] * (n+1)
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + lst[i]

for _ in range(m):
    i, j = map(int, input().split())
    segment_sum = prefix_sum[j] - prefix_sum[i-1]
    print(segment_sum)