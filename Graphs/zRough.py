if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        l = list(map(int, input().split()))
        l.sort(reverse=True)
        if l[-1]==0:
            ans = len(l) - l.count(0)
        else:
            last_ele = l[-1]
            ans = len(l)*last_ele
            for i in l:
                if i - last_ele <= 0:
                    break
                ans += 1
        print(ans)
