import sys
input = sys.stdin.readline

count = 0

n,k = map(int, input().split())
money_types = []
for i in range(n):
    money_types.append(int(input()))

money_types.reverse()

for money in money_types:
    count += k // money
    k %= money

print(count)