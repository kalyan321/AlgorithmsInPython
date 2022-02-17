import heapq


def closestKElem():
    res = []
    for i in arr:
        res.append([abs(i - x), i])
    ans = []
    res.sort(key=lambda x:(x[0],x[1]))
    # for i in range(k):
    #     ans.append(heapq.heappop(res)[1])
    # ans.sort()
    print(res)


if __name__ == "__main__":
    arr = [0, 2, 1, 4, 5]
    k = 1
    x = 1
    closestKElem()
