exp = input().split('-')

num = []
for i in exp:
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)
    num.append(sum)

print(tmp)