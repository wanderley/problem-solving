"""
Reference: https://cp-algorithms.com/string/z-function.html
"""
from functools import reduce

class Solution:
    def sumScores(self, s: str) -> int:
        return reduce(lambda a, b: a + b, z_function(s), len(s))

def z_function(s):
    n = len(s)
    l = r = 0
    z = [0] * n
    for i in range(1, n):
        assert l <= r, "rightest longest prefix (RLP) of S: l=%d r=%d" % (l, r)
        assert l <= i, "RLP always start before ith char"
        if i > r:
            # We can't reuse anything from the last longest prefix.
            #
            #   0 1 2 3 4 ... 5 6 7
            #         l-------r
            #                   i
            z[i] = 0
            while i + z[i] < n and s[i + z[i]] == s[z[i]]:
                z[i] += 1
            if i + z[i] - 1 > i:
                # the palindrome starting on i is the RLP one
                l, r = i, i + z[i] - 1
        else:
            # The RLP passes over the ith character and we might not be able to
            # reuse it.
            #
            #   0 1 2 3 4 ... 5 6 7
            #         l-------r
            #         i
            #             i
            #                 i
            #
            # We know that
            #   1. s[i] = s[i-l]
            #   2. z[i-l] is already computed with the length of the longest
            #      prefix of s
            #
            # Note that bootstrap z[i] with z[i-l] because we don't know nothing
            # about matching on s[r...(n-1)].
            #
            #   0 1 2 3 4 ... 5 6 7
            #         l-------r
            #         i           ^
            #                     i+z[i-l]
            assert i <= r
            z[i] = min(z[i-l], r-i+1)
            while i + z[i] < n and s[i + z[i]] == s[z[i]]:
                z[i] += 1
            if i + z[i] - 1 > i:
                l, r = i, i + z[i] - 1
    return z
