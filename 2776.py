import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    note_1 = sorted(list(map(int,input().split())))
    m = int(input())
    note_2 = list(map(int,input().split()))
    for i in range(m):
        left = 0
        right = len(note_1) - 1
        found = False

        while left <= right:
            mid = (left + right) //2
            if note_1[mid] == note_2[i]:
                print('1')
                found = True
                break
            elif note_1[mid] < note_2[i]:
                left = mid +1
            else:
                right = mid -1
        if not found:
            print('0')