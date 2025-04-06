import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
targets = list(map(int, input().split()))

for i in range(m):
    left = 0 
    right = len(a) - 1
    found = False
    
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == targets[i]:
            print('1')
            found = True
            break
        elif a[mid] < targets[i]:  
            left = mid + 1
        else:  
            right = mid - 1
    
    if not found:
        print('0')