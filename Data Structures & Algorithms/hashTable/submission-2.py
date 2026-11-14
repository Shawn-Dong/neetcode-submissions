class Pair:
    def __init__(self, key, value):
        self.key = key
        self.val = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.buckets: list[list[Pair]] = [[]for _ in range(capacity)]

    def _index(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self._index(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                pair.val = value
                return
        new_pair = Pair(key, value)
        bucket.append(new_pair)
        self.size += 1
        lc = self.size/self.capacity
        if lc >= 0.5:
            self.resize()


    def get(self, key: int) -> int:
        index = self._index(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                return pair.val
        return -1


    def remove(self, key: int) -> bool:
        index = self._index(key)
        bucket = self.buckets[index]
        for i in range(len(bucket)):
            if bucket[i].key == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False


    def getSize(self) -> int:
        return self.size

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_buckets : List[List[Pair]] = [[]for _ in range(new_capacity)]
        for bucket in self.buckets:
            for pair in bucket:
                new_index = pair.key % new_capacity
                new_buckets[new_index].append(pair)
        self.buckets = new_buckets
        self.capacity = new_capacity


    def getCapacity(self) -> int:
        return self.capacity



