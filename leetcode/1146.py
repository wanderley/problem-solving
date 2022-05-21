class SnapshotArray:

    def __init__(self, length: int):
        self._values = []
        for i in range(length):
            self._values.append([[0, 0]])
        self._snap_id = 0

    def set(self, index: int, val: int) -> None:
        if self._values[index][-1][0] != self._snap_id:
            self._values[index].append([self._snap_id, 0])
        self._values[index][-1][1] = val

    def snap(self) -> int:
        self._snap_id += 1
        return self._snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        lo, hi = 0, len(self._values[index]) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            mid_snap_id = self._values[index][mid][0]
            if mid_snap_id == snap_id:
                return self._values[index][mid][1]
            elif mid_snap_id > snap_id:
                hi = mid - 1
            else:
                lo = mid + 1
        return self._values[index][lo - 1][1]
