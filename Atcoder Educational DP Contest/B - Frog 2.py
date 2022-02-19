if __name__ == "__main__":
    n, k = map(int, input().split())
    costs = list(map(int, input().split()))
    dp = [float('inf') for i in range(n)]
    dp[0] = 0
    for i in range(n):
        j = i + 1
        for j in range(i+1, i+k+1):
            if j < n:
                dp[j] = min(dp[j], dp[i] + abs(costs[j] - costs[i]))
    print(dp[-1])
