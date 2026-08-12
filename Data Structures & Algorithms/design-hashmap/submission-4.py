class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.hash_map =[[] for _ in range(self.size)]
    
    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        for elem in self.hash_map[index]:
            if elem[0] == key:
                elem[1] = value
                return
        self.hash_map[index].append([key, value])

    def get(self, key: int) -> int:
        index = self._hash(key)
        for elem in self.hash_map[index]:
            if elem[0] == key:
                return elem[1]
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        for idx, elem in enumerate(self.hash_map[index]):
            if elem[0] == key:
                self.hash_map[index].pop(idx)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)