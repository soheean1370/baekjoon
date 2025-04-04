import sys
input = sys.stdin.readline

n = int(input())
lines = []

for _ in range(n):
    a, b = map(int,input().split())
    lines.append([a,1])
    lines.append([b-0.1,-1])

lines.sort(key= lambda x: x[0])

result = [0]
temp = 0

for i in lines:
    temp += i[1]
    result.append(temp)

print(max(result))