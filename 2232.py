class Solution:
    def minimizeResult(self, expression: str) -> str:
        left, right = expression.split("+")
        to_int = lambda d: 1 if d == '' else int(d)
        lc = [(left[0:i], left[i:]) for i in range(len(left))]
        rc = [(right[0:i], right[i:]) for i in range(len(right), 0, -1)]
        candidates = sorted(
            [
                (
                    (to_int(l[0]))*(to_int(l[1])+to_int(r[0]))*to_int(r[1]),
                    f"{l[0]}({l[1]}+{r[0]}){r[1]}",
                )
                for l in lc
                for r in rc
            ],
            key=lambda e: e[0]
        )
        return candidates[0][1]
