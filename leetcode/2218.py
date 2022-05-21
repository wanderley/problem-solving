from typing import List
from functools import lru_cache

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @lru_cache(None)
        def rec(k, i):
            if k <= 0 or i == len(piles):
                return 0

            ret = rec(k, i+1)
            acc = 0
            for n in piles[i]:
                acc += n
                k   -= 1
                if k < 0:
                    break
                ret = max(ret, acc + rec(k, i+1))
            return ret

        return rec(k, 0)


Solution().maxValueOfCoins(piles=[[1,100,3],[7,8,9]], k=2)
Solution().maxValueOfCoins(piles=[[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k=7)
