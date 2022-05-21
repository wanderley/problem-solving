from itertools import filterfalse

class Solution:
    def _nums(self, num:int):
        digits = [int(d) for d in str(num)]
        is_even = lambda d: (d % 2) == 0
        e, o = reversed(sorted(filter(is_even, digits))), reversed(sorted(filterfalse(is_even, digits)))
        for d in digits:
            if is_even(d):
                yield next(e)
            else:
                yield next(o)
    def largestInteger(self, num: int) -> int:
        return int("".join([str(d) for d in self._nums(num)]))


assert Solution().largestInteger(1234) == 3412
