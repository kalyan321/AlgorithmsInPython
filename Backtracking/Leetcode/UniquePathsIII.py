import bisect
import math

for _ in range(int(input())):
    n, k = map(int, input().split())
    l = []
    i = 1
    ans = -1
    while i <= math.sqrt(n):
        if n % i == 0:
            if n // i <= k:
                ans = n // i
                break
            l.append(i)
        i += 1

    if ans == -1:
        for i in range(len(l) - 1, -1, -1):
            if n % l[i] == 0 and l[i] <= k:
                ans = l[i]
                break
    print(n // ans)
