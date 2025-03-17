import sys
input = sys.stdin.readline

n,k = map(int, input().split())
temp_list = list(map(int, input().split()))

# 첫 구간의 합을 먼저 구함
window_sum = sum(temp_list[:k])
max_sum = window_sum

# 슬라이딩 윈도우 방식으로 한칸씩 이동하며 계산

for i in range(1,n-k+1):
    window_sum = window_sum - temp_list[i -1] + temp_list[i+k-1]
    max_sum = max(max_sum, window_sum)

print(max_sum)