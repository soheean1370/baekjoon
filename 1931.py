import sys
input = sys.stdin.readline

n = int(input())
full_time = []

for _ in range(n):
    full_time.append(list(map(int, input().split())))
    

full_time = sorted(full_time)    
end = full_time[0][1] 
cnt = 1

for i in range( 1, len(full_time)):
    if full_time[i][1] >= end:
        cnt += 1
        end = full_time[i][1] 

print(cnt)