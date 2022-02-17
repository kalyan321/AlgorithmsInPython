import bisect


def binary_search_right(lst, target, low=0, high=None):
    if high is None:
        high = len(lst)
    while low < high:
        mid = (low + high) // 2
        if lst[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low


if __name__ == '__main__':
    l = [0, 1, 2, 3, 3, 3, 4, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8]
    print(bisect.bisect_right(l, 4))
    print(binary_search_right(l, 4))
    # print(bisect.bisect_right(l, 3))
