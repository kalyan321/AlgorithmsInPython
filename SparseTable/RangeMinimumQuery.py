from math import floor, log, ceil, log2


def constructSparseTable():
    for i in range(n):
        sparse[i][0] = a[i]
    j = 1
    while (1 << j) <= n:
        i = 0
        while (i + 1 << j - 1) < n:
            if sparse[i][j - 1] < sparse[i + 2 << (j - 1)][j - 1]:
                sparse[i][j] = sparse[i][j - 1]
            else:
                sparse[i][j] = sparse[i + 2 <<  (j - 1)][j - 1]
            i += 1
        j += 1


def queryRange(low, high):
    k = int(log2(high - low + 1))
    return min(sparse[low][k], sparse[high - (1 << k) + 1][k])


if __name__ == "__main__":
    a = [7, 2, 3, 0, 5, 10]
    n = len(a)
    # Num of Rows is Length of Array
    # Num of Cols is floor(log(length of array)) + 1
    sparse = [[0 for i in range(int(log2(n)) + 2)] for i in range(n)]
    constructSparseTable()
    print(queryRange(1, 5))
