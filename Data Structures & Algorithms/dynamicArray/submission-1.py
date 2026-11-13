class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
            self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.capacity == self.size:
            self.resize()
        self.arr[self.size] = n
        self.size +=1


    def popback(self) -> int:
        val = self.arr[self.size-1]
        self.size -= 1
        return val 

    def resize(self) -> None:
        nc = self.capacity * 2
        self.capacity = nc
        new = [0]* nc
        for i in range(self.size):
            new[i] = self.arr[i]
        self.arr = new


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
