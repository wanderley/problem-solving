class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nums = [
                (nums[i] + nums[i+1]) % 10
                for i in range(len(nums)-1)
            ]
        return nums[0]

assert Solution().triangularSum(nums=[1,2,3,4,5]) == 8
assert Solution().triangularSum(nums=[5]) == 5
