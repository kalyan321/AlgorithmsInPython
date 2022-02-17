# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

def isValid(r, c):
    return 0 <= r < len(mat) and 0 <= c < len(mat[0])


def getPaths(r, c):
    return [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]


def lip(r, c):
    if visited[r][c] != -1:
        return visited[r][c]
    ans = 1
    paths = getPaths(r, c)
    for path in paths:
        count = 0
        if isValid(path[0], path[1]):
            if mat[r][c] < mat[path[0]][path[1]]:
                count = 1 + lip(path[0], path[1])
        ans = max(count, ans)
    visited[r][c] = ans
    return ans


if __name__ == "__main__":
    mat = [[7, 7, 5], [2, 4, 6], [8, 2, 0]]
    maxi = 1
    visited = [[-1 for i in range(len(mat[0]))] for i in range(len(mat))]
    ans = 1
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            ans = max(lip(i, j), ans)
    print(ans)
