from collections import Counter
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = zip(*matches)
        all_players = set(winners + losers)
        return [
            sorted(all_players - set(losers)),
            sorted([
                loser
                for loser, count in Counter(losers).items()
                if count == 1
            ])
        ]

assert Solution().findWinners(
    [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
) == [[1, 2, 10], [4, 5, 7, 8]]
