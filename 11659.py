import sys

n, m = map(int,input().split())
lst = list(map(int, input().split()))
sum_lst = []
for _ in range(m):
    i,j = map(int, input().split())
    sum_lst.append(sum(lst[i-1:j]))
    print(sum_lst[_])