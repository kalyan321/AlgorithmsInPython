# problem description : https://atcoder.jp/contests/dp/tasks/dp_a


if __name__ == "__main__":
    num = int(input())
    costs = list(map(int, input().split()))
    dp = [float('inf')] * num
    dp[0] = 0
    for i in range(1, num):
        if i == 1:
            dp[i] = abs(costs[i] - costs[i-1]) + dp[i-1]
        else:
            dp[i] = min(abs(costs[i] - costs[i-1]) + dp[i-1], abs(costs[i] - costs[i-2]) + dp[i-2])
    print(dp[-1])
