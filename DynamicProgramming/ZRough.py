from collections import defaultdict


def bfs():
    v[x] = 1
    q = [[x]]
    while q:
        path = q.pop(0)
        if path[-1] == y:
            print(len(path))
            print(*path)
            return
        for i in g[path[-1]]:
            if v[i] == 0:
                q.append(path + [i])
                v[i] = 1


n, m, t, c = map(int, input().split())
g = defaultdict(list)
v = defaultdict(int)
for i in range(m):
    u, ve = map(int, input().split())
    g[u].append(ve)
    g[ve].append(u)
x, y = map(int, input().split())
bfs()