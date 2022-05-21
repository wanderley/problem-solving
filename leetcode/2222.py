from itertools import accumulate

class Solution:
    def numberOfWays(self, s: str) -> int:
        oz, zo, zs, os, ways = 0, 0, 0, 0, 0
        for d in s:
            if d == "0":
                zs += 1
                oz += os
                ways += zo
            else:
                os += 1
                zo += zs
                ways += oz
        return ways

    def numberOfWays_AC_SLOW(self, s: str) -> int:
        N = len(s)
        zc = list(accumulate(s[::-1], lambda ac, v: ac + (1 if v == "0" else 0), initial=0))[::-1]
        oc = list(accumulate(s[::-1], lambda ac, v: ac + (1 if v == "1" else 0), initial=0))[::-1]
        assert len(zc) == N+1
        assert len(oc) == N+1
        oz, zo = [0], [0]
        for i in range(N-1, -1, -1):
            if s[i] == "0":
                oz.append(oz[-1])
                zo.append(zo[-1] + oc[i+1])
            else:
                oz.append(oz[-1] + zc[i+1])
                zo.append(zo[-1])
        oz.reverse()
        zo.reverse()
        ways = 0
        for i, d in enumerate(s):
            if d == "0":
                ways = ways + oz[i+1]
            else:
                ways = ways + zo[i+1]
        return ways

    def numberOfWays_SLOW_DP(self, s: str) -> int:
        zeros = list(accumulate(s[::-1], lambda ac, v: ac + (1 if v == "0" else 0), initial=0))[1:][::-1]
        ones = list(accumulate(s[::-1], lambda ac, v: ac + (1 if v == "1" else 0), initial=0))[1:][::-1]
        memo = {}
        def rec(last, size, i):
            key = (last, size, i)
            if key in memo:
                return memo[key]
            if i == len(s):
                return 0
            if size == 2:
                return ones[i] if last == "0" else zeros[i]

            memo[key] = rec(last, size, i + 1)
            if last != s[i]:
                memo[key] = memo[key] + rec(s[i], size + 1, i + 1)
            return memo[key]

        return rec("$", 0, 0)


"""
s   0 0 1 1 0 1 0 0 1 1 0 1
z<  6 5 4 4 4 3 3 2 1 1 1 0 0
o<  6 6 6 5 4 4 3 3 3 2 1 1 0
oz        9 5 5 2 2 2 1 0 0   (z<[i+1]+oz[i+1] if s[i] == 1 else oz[i+1])
zo                4 1 1 1 0
"""


assert Solution().numberOfWays("001101") == 6
assert Solution().numberOfWays("11100") == 0
