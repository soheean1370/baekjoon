import sys
input = sys.stdin.readline

x,y = map(int,input().split())

z=(100*y)//x
left = 0
right = x
result = left

if z>=99:
    print(-1)

else:
    while left <= right:
        mid = (left+right)//2
        if (100 *(y+mid))//(x+mid) > z:
            result = mid
            right = mid -1
        else:
            left =mid +1

    print(mid)