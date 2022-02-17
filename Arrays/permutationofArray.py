def permutation(l, per):
    if not l:
        res.append(per)
    for i in range(len(l)):
        permutation(l[:i] + l[i + 1:], per + [l[i]])


if __name__ == '__main__':
    res = []
    lst = [1, 2]
    permutation(lst, [])
    print(res)
