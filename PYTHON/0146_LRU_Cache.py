# 23/09/2026
# Medium
# LeetCode 146: LRU Cache using native ordered dictionary properties.

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache.pop(key)
        self.cache[key] = val
        return val
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            oldest = next(iter(self.cache))
            self.cache.pop(oldest)
if __name__ == "__main__":
    obj = LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1)) 
    obj.put(3, 3) 
    print(obj.get(2)) 
    obj.put(4, 4) 
    print(obj.get(1)) 
    print(obj.get(3)) 
    print(obj.get(4))