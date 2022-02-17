l = list(map(int,input().split()))
l.sort(reverse=True)
ans = l[0]
for i in range(1,len(l)):
    if i >= 0:
        t = l[i]
        l[i] += l[i-1] + ans
        ans += t
print(l)
