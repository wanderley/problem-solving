from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        itn = {}
        for i in range(len(nums)):
            itn[nums[i]] = itn.get(nums[i], set()) | {i}
        for i in range(len(nums)):
            rest = target - nums[i]
            candidates = itn.get(rest, set()) - {i}
            if len(candidates) > 0:
                return [i, candidates.pop()]

    def twoSum_slow(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
