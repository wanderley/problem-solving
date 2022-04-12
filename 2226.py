from typing import List

class Solution:
    def _valid(self, candies: List[int], k: int, ps: int) -> bool:
        for pile in candies:
            k = k - pile // ps
            if k <= 0:
                return True
        return False

    def maximumCandies(self, candies: List[int], k: int) -> int:
        start = 0
        end = max(candies)
        while start != end:
            mid = start + (end - start + 1) // 2
            if self._valid(candies, k, mid):
                start = mid
            else:
                end = mid - 1
        return start


assert Solution().maximumCandies([5,8,6], 3) == 5
assert Solution().maximumCandies([2,5], 11) == 0
