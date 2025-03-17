import sys
input = sys.stdin.readline

n,k = map(int, input().split())

temp_list = list(map(int, input().split()))

result = []
for i in range(n - k +1):
    result.append(sum(temp_list[i:i+k]))

print(max(result))