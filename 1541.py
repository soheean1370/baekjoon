exp = input().split('-')

num = []
for i in exp: # [55, 50+40]
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)
    num.append(sum) # [55, 90]

n = num[0]
for i in range(1, len(num)):
    n -= num[i]

print(n )