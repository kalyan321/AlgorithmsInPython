def initlize(n):
    size = 1
    while size < n:
        size = size << 1
    arr = [float('inf')] * (2 * size - 1)
    return arr


def constructSegmentTree(inputArr, segArr, low, high, pos):
    if low == high:
        segArr[pos] = inputArr[low]
        return
    mid = (low + high) // 2
    constructSegmentTree(inputArr, segArr, low, mid, 2 * pos + 1)
    constructSegmentTree(inputArr, segArr, mid + 1, high, 2 * pos + 2)
    segArr[pos] = min(segArr[2 * pos + 1], segArr[2 * pos + 2])


def updateSegmentTree():
    pass


def rangeMinQuery(segArr, qlow, qhigh, low, high, pos):
    if qlow <= low and qhigh >= high:
        return segArr[pos]
    if qlow > high or qhigh < low:
        return float('inf')
    mid = (low + high) // 2
    return min(rangeMinQuery(segArr, qlow, qhigh, low, mid, 2 * pos + 1),
               rangeMinQuery(segArr, qlow, qhigh, mid + 1, high, 2 * pos + 2))


if __name__ == '__main__':
    n = int(input())
    inputArr = list(map(int, input().split()))
    segArr = initlize(n)
    constructSegmentTree(inputArr, segArr, 0, n - 1, 0)
    ans = rangeMinQuery(segArr, 1, 5, 0, 5, 0)
    print(ans)
