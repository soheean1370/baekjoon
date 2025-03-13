n = int(input())

dp = [[0 ]* 10 for _ in range(n+1)]

for i in range(1,10):
    dp[1][i] = 1


for i in range(2, n+1):
    for j in range(10):
        # 가장 뒤에 오는 숫자가 0일땐, 그 앞에 1만 올 수 있음
        if(j == 0):
            dp[i][j] = dp[i-1][1]
        
        # 가장 뒤에 오늘 숫자가1~8일땐, 그 앞에 +-1이 올 수 있음
        elif(1 <= j <= 8):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        
        #가장 뒤에 오는 숫자가 9일땐, 그 앞에 8만 올 수 있음
        elif (j == 9):
            dp[i][j] = dp[i-1][8]

print(sum(dp[n])%1000000000)