import sys
input = sys.stdin.readline

n = int(input())
full_time = []

for _ in range(n):
    full_time.append(list(map(int, input().split())))
    

full_time.sort(key=lambda x: x[1])  # 종료 시간 기준으로 정렬 
end = full_time[0][1] 
cnt = 1

for i in range( 1, len(full_time)):
    if full_time[i][0] >= end:
        cnt += 1
        end = full_time[i][1] 

print(cnt)