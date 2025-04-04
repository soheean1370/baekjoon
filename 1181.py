n = int(input())
words = []

for _ in range(n):
    temp = input()
    words.append(temp)

words.sort()

print(*words)