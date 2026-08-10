class TimeMap:

    def __init__(self):
        self._time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._time_map[key].append([value, timestamp])
        print(self._time_map)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._time_map:
            return ''

        to_process = self._time_map[key]

        l, r = 0, len(to_process)-1
        res = ''
        while l <= r:
            mid = (l + r) // 2
            if timestamp < to_process[mid][1]:
                r = mid - 1
            else:
                res = to_process[mid][0]
                l = mid + 1
        return res