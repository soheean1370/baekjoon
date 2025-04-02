import sys
input = sys.stdin.readline

n = int(input())
lst = [0] * n
for i in range(n):
    lst[i] = int(input())
    
lst = sorted(lst,reverse=False)

for j in range(n):
    print(lst[j])