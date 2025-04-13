import sys
input = sys.stdin.readline


n = int(input())
budget = list(map(int, input().split()))
m = int(input())

start = 1
end = max(budget)
max_budget = 0
while start <= end:
    mid = (start + end) //2
    total = 0

    for i in budget:
        total += min(i,mid)
    
    if total <= m:
        start = mid + 1
        max_budget = mid
    
    else:
        end = mid -1

print(max_budget)
