# #
# # Problem Statement :
# #     print all subsequences of string
# #
# # Example 1 :
# # Input : abc
# # Output : a, b, c, ab, ac, bc, abc
# #
# # Input : aab
# # Output : a, b, aa, ab, aab
#
# Solution :

def subsequence(s, binary, length):
    sub = ""
    for i in range(length):
        # check if ith bit in binary is 1
        if binary & (1 << i):
            sub += s[i]
    return sub


s = input().strip()
length = len(s)
limit = 2 ** length
result = []
for i in range(1, limit):
    sub = subsequence(s, i, length)
    result.append(sub)
print(*result)
