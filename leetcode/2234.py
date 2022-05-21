from typing import List
from bisect import bisect_left

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        N = len(flowers)
        flowers = sorted(flowers)
        to_level = []
        for i, f in enumerate(flowers):
            to_level.append(0 if i == 0 else to_level[i-1] + (flowers[i] - flowers[i-1]) * i)

        if min(flowers) >= target:
            return N * full
        j, ret, planted_flowers = N, 0, 0
        while j > -1:
            newFlowers = newFlowers - (0 if j == N else max(target - flowers[j], 0))
            completed_gardens = N - j
            j = j - 1
            if newFlowers <= 0:
                break
            i = min(bisect_left(to_level, newFlowers), j+1)
            if i == 0:
                ret = max(ret, completed_gardens * full)
                continue
            available_to_plant = min(
                (newFlowers - to_level[i-1]) // i,
                target - flowers[i-1] - 1
            )
            to_be_planted = to_level[i-1] + available_to_plant * i
            assert to_be_planted <= newFlowers
            min_flowers = flowers[i-1] + available_to_plant
            assert min_flowers < target
            ret = max(ret, completed_gardens * full + min_flowers * partial)

        return ret

[
    Solution().maximumBeauty(flowers=[1,3,1,1], newFlowers=7, target=6, full=12, partial=1),
    Solution().maximumBeauty(flowers=[2,4,5,3], newFlowers=10, target=5, full=2, partial=6),
    Solution().maximumBeauty(flowers=[8,20,13], newFlowers=12, target=12, full=4, partial=3),
    Solution().maximumBeauty(flowers=[13], newFlowers=18, target=15, full=9, partial=2),
] == [14, 30, 41, 28]
