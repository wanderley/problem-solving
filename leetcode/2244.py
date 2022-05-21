from collections import Counter
from functools import lru_cache

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        @lru_cache(None)
        def dp(num):
            if num == 0:
                return 0
            if num < 0:
                return 10**5
            return min(dp(num-2), dp(num-3)) + 1
        ret = 0
        for num, count in Counter(tasks).items():
            ret += dp(count)
        return -1 if ret >= 10**5 else ret
