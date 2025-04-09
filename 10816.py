import sys
input = sys.stdin.readline

n = int(input())
num_cards = list(map(int, input().strip().split()))
m = int(input())
find_cards = list(map(int, input().strip().split()))

cnt_dic = {}

for i in num_cards:
    if i in cnt_dic:
        cnt_dic[i] += 1
    else:
        cnt_dic[i] = 1

for j in find_cards:
    if j in cnt_dic:
        print(cnt_dic[j], end =' ')
    else:
        print(0,end=' ')