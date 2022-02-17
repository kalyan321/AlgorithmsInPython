from collections import defaultdict
for _ in range(int(input())):
    mod = 10**9 + 7
    n = int(input())
    l = list(map(int,input().split()))
    d = defaultdict(int)
    count = 0
    ans = 1
    for i in l:
        if d[i] == 0:
            count += 1
        d[i] += 1
    for i in d:
        ans = ans *(d[i] + 1)
        ans = ans % mod
    print(ans-1)