import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    cnt = 0
    start = 0

    N,M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = sorted(list(map(int,input().split())))

    for i in range(N):
        while True:
            if start == M or A[i] <= B[start]: # B를 끝까지 다 봤거나 A[i] 보다 작은 원소가 없다
                cnt += start
                break
            else:
                start += 1
    print(cnt)
    


