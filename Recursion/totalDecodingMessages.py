from functools import lru_cache


@lru_cache(None)
def totaldecodingMessages(s, sub, pos):
    if len(sub) > 0 and int(sub) > 26:
        return 0
    if pos == len(s):
        return 1
    return totaldecodingMessages(s, s[pos], pos + 1) + totaldecodingMessages(s, sub + s[pos], pos + 1)


if __name__ == '__main__':
    ans = totaldecodingMessages('111111111111111111111111111111111111111', '1', 1)
    print(ans)
