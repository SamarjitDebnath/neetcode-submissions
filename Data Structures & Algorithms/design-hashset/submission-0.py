class MyHashSet:

    def __init__(self):
        self.size = 10000 # atmost 10000 calls 
        self.hashset = [set() for _ in range(self.size)]
    
    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        index = self._hash(key)
        self.hashset[index].add(key)
        print(self.hashset[index])

    def remove(self, key: int) -> None:
        index = self._hash(key)
        if key in self.hashset[index]:
            self.hashset[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        return True if key in self.hashset[index] else False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)