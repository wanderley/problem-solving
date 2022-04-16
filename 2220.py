class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while start > 0 or goal > 0:
            a, b = start & 1, goal & 1
            if a != b:
                count = count + 1
            start = start >> 1
            goal = goal >> 1
        return count


Solution().minBitFlips(start=10, goal=7)
Solution().minBitFlips(start=3, goal=4)
