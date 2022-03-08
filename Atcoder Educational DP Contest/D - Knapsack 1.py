if __name__ == "__main__":
    n, w = map(int,input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort(key = lambda x:x[0])
    dp = [[0 for i in range(w+1)] for i in range(n)]
    for i in range(n):
        for j in range(1, w+1):
            if j < l[i][0]:
                if i == 0:
                    dp[i][j] = l[i][1]
                else:
                    dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], l[i][1] + dp[i-1][j-l[i][0]])
    print(dp[-1][-1])
