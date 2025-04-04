import sys
input = sys.stdin.readline

n = int(input())
numbers = {}

for _ in range(n):
    k = int(input())
    if numbers.get(k,'none') == "none":
        numbers[k] = 1
    else:
        numbers[k] += 1

temp = list(numbers.keys())
temp.sort()

for i in temp:
    for j in range(numbers[i]):
        print(i)