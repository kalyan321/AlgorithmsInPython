import sys

sys.setrecursionlimit(1500)


def minimum(n, dp):
    if dp[n] != -1:
        return dp[n]
    val = minimum(n - 1, dp)
    if n % 3 == 0:
        val = min(minimum(n // 3, dp), val)
    if n % 2 == 0:
        val = min(minimum(n // 2, dp), val)
    dp[n] = 1 + val
    return dp[n]


if __name__ == "__main__":
    n = int(input())
    dp = [-1] * (n + 1)
    dp[1] = 0
    ans = minimum(n, dp)
    # print(dp)
    print(ans)
