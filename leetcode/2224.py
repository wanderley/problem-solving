class Solution:
    def _convert(self, time: str) -> int:
        nums = time.split(":")
        return int(nums[0]) * 60 + int(nums[1])

    def convertTime(self, current: str, correct: str) -> int:
        ret   = 0
        start = self._convert(current)
        end   = self._convert(correct)
        diff  = end - start

        ret  = ret + (diff // 60)
        diff = diff - (diff // 60) * 60
        ret  = ret + (diff // 15)
        diff = diff - (diff // 15) * 15
        ret  = ret + (diff // 5)
        diff = diff - (diff // 5) * 5
        ret  = ret + diff

        return ret

assert Solution().convertTime("02:30", "04:35") == 3
assert Solution().convertTime("11:00", "11:01") == 1
