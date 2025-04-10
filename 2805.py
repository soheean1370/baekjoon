import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
start = 0
end = max(tree)

while start <= end:
    mid = (start + end) // 2
    total = 0
    
    # 한 번의 반복문으로 total 계산
    for height in tree:
        if height > mid:
            total += height - mid
        
        # 최적화: 이미 m을 넘어섰다면 더 계산할 필요 없음
        if total > m:
            break
    
    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(end)  # 주의: result 대신 end를 출력