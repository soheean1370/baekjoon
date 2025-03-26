import sys
input = sys.stdin.readline

# 입력받기: 동전 종류 개수(n)와 목표 금액(k)
# map을 사용해 입력된 문자열을 정수로 변환
n, k = map(int, input().split())

# 사용 가능한 동전 종류를 저장할 리스트
money_types = []

# n번 반복하며 각 동전의 금액 입력받기
for _ in range(n):
    # 각 동전 금액을 money_types 리스트에 추가
    money_types.append(int(input()))

# 동적 계획법(DP) 배열 초기화
# k+1 크기의 배열을 0으로 채움 (0원부터 k원까지)
dp = [0 for i in range(k + 1)]

# 0원을 만드는 경우의 수는 1로 초기화 
# (아무 동전도 사용하지 않는 경우)
dp[0] = 1

# 각 동전 종류에 대해 반복
for money in money_types:
    # money원부터 k원까지 각 금액에 대해 반복
    for i in range(money, k+1):
        # 현재 금액(i)을 만드는 경우의 수에
        # (현재 금액 - 현재 동전 금액)을 만드는 경우의 수를 더함
        dp[i] += dp[i-money]

# 최종적으로 k원을 만드는 전체 경우의 수 출력
print(dp[k])