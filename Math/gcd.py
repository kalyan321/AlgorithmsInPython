walks = 0
for i in range(10):
    visited = 3
    if i%2 ==0:
        visited = 2
    t = 3
    walks += visited == t
print(walks)