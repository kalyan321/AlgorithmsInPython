def find_upper_bound(low, high, ele):
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= ele :
            low = mid + 1
        else:
            high = mid
    return low


if __name__ == '__main__':
    arr = [1,2]
    x = find_upper_bound(0, len(arr),arr[0])
    count = 1
    while x < len(arr):
        x = find_upper_bound(x, len(arr), arr[x])
        count += 1
    print(count)