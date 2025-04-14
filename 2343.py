import sys
input = sys.stdin.readline 

n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
nums = list(map(int, input().split()))


for i in range(m):
    left = 0
    right = len(cards) - 1
    found = False

    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == nums[i]:
            print('1')
            found = True
            break
        elif cards[mid] < nums[i]:  
            left = mid + 1
        else:  
            right = mid - 1
    
    if not found:
        print('0')