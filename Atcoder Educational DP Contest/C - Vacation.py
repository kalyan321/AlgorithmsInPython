if __name__ == "__main__":
    n = int(input())
    happiness = [list(map(int, input().split())) for i in range(n)]
    for i in range(1, n):
        for j in range(3):
            if j == 0:
                happiness[i][j] += max(happiness[i-1][j+1], happiness[i-1][j+2])
            elif j == 1:
                happiness[i][j] += max(happiness[i-1][j-1], happiness[i-1][j+1])
            else:
                happiness[i][j] += max(happiness[i-1][j-1], happiness[i-1][j-2])
    print(max(happiness[-1]))

