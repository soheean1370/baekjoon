
# 모르겠다 다시한번 풀어보자

import sys
input = sys.stdin.readline

first = ' ' + input().strip()
second = ' ' + input().strip()

# LCS(Longest Common Subsequence, 최장 공통 부분 수열) 계산을 위한 DP 테이블 초기화
# dp[i][j]는 first의 첫 i개 문자와 second의 첫 j개 문자로 만들 수 있는 LCS의 길이를 저장
dp = [[0 for _ in range(len(second))] for _ in range(len(first))]

# first의 문자들을 순차적으로 탐색 (i는 1부터 시작, 0은 공백 문자로 인해 비워둠)
for i in range(1, len(first)):
    # second의 문자들을 순차적으로 탐색 (j는 1부터 시작)
    for j in range(1, len(second)):
        # 두 문자가 같으면, 이전까지의 LCS 길이에 1을 더함
        if first[i] == second[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        # 두 문자가 다르면, 이전 단계 중 더 긴 LCS 값을 가져옴
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# dp 테이블의 마지막 값(dp[-1][-1])이 최장 공통 부분 수열의 길이
print(dp[-1][-1])
