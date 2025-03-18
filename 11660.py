import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [0]
for i in range(n):
    line = [0]+ list(map(int,input().split()))
    arr.append(line)

# print(arr)
sum_arr = [[0] * (n+1) for _ in range(n+1)]
# print(sum_arr)

for i in range(1,n+1):
    for j in range(1,n+1):
        sum_arr[i][j] = arr[i][j]
        sum_arr[i][j] += sum_arr[i][j-1] + sum_arr[i-1][j]
        sum_arr[i][j] -= sum_arr[i-1][j-1]

# print(sum_arr)

for _ in range(m):
    x1, y1, x2, y2 = map(int,input().split())
    ans =sum_arr[x2][y2]
    ans -= sum_arr[x1-1][y2]
    ans -= sum_arr[x2][y1-1]
    ans += sum_arr[x1-1][y1-1]
    print(ans)