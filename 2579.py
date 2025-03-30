n = int(input())  # 계단 개수 입력

s = [int(input()) for _ in range(n)]  # 각 계단의 점수 입력

if n <= 2:  
    print(sum(s))  # 계단이 1개 또는 2개일 때는 그냥 다 밟음
else:
    dp = [0] * n  # DP 테이블 초기화
    dp[0] = s[0]  # 첫 번째 계단 점수
    dp[1] = s[0] + s[1]  # 두 번째 계단까지의 최대 점수

    for i in range(2, n):
        dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])

    print(dp[-1])  # 마지막 계단까지 갔을 때의 최대 점수
