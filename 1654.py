import sys
input = sys.stdin.readline

k,n = map(int,input().split())

lan = [int(input()) for _ in range(k)]

# start: 제일 짧은 길이 end: 랜선 중 가장 긴 길이
start= 1
end = max(lan)

while start <= end:
    # mid : 만들고 싶은 래선의 길이
    mid = (start + end) // 2
    lines = 0

    for i in lan:
        lines += i // mid

    # 만약 만들고 싶은 수 이상으로 만들어지면 랜선 길이를 더 길게
    if lines >= n:
        start = mid + 1
    
    else:
        end = mid -1

print(end)