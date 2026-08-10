class TimeMap:

    def __init__(self):
        self.kvStore = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.kvStore:
            self.kvStore[key].append([value, timestamp])
        else:
            self.kvStore[key] = [[value, timestamp]]
        print(self.kvStore)

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        if key not in self.kvStore:
            return res
        
        toProcess = self.kvStore[key]
        
        l, r = 0, len(toProcess)-1
        while l <= r:
            mid = l + (r - l) // 2
            if toProcess[mid][1] <= timestamp:
                res = toProcess[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
        