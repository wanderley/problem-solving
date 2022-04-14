from typing import List
from heapq import heappush, heappop

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        pq = []
        for n in nums:
            heappush(pq, n)
        while k > 0:
            e1 = heappop(pq)
            e = e1 + 1
            k = k - 1
            heappush(pq, e)

        ret = 1
        while len(pq) > 0:
            ret = (ret * heappop(pq)) % (10**9 + 7)
        return ret


assert Solution().maximumProduct([0,4], 5) == 20
assert Solution().maximumProduct([6,3,3,2], 2) == 216
