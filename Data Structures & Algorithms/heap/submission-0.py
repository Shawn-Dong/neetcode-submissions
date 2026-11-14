class MinHeap:
    
    def __init__(self):
        self.heap = []
        

    def push(self, val: int) -> None:
        self.heap.append(val)
        location = len(self.heap) - 1

        while location != 0:
            parent = (location - 1) // 2
            if self.heap[location] < self.heap[parent]: 
                self.heap[parent], self.heap[location] = self.heap[location], self.heap[parent]
                location = parent
            else:
                break

    def pop(self) -> int:
        if len(self.heap) == 0:
            return -1

        smallest = self.heap[0]
        replacement = self.heap.pop()

        if len(self.heap) > 0:
            self.heap[0] = replacement
            location = 0
            while True:
                left = 2 * location + 1
                right =2 * location + 2
                if left >= len(self.heap):
                    break
                smaller_child = left
                if right < len(self.heap) and self.heap[right] < self.heap[left]:
                    smaller_child = right
                if self.heap[location] > self.heap[smaller_child]:
                    self.heap[location], self.heap[smaller_child] = self.heap[smaller_child], self.heap[location]
                    location = smaller_child
                else:
                    break
        return smallest 
        
    
        

    def top(self) -> int:
        if len(self.heap) == 0:
            return -1
        smallest = self.heap[0]
        return smallest
        

    def heapify(self, nums: List[int]) -> None:
        self.heap = nums
        start = len(self.heap) // 2 - 1
        while start >= 0:
            self._sift_down(start)
            start -= 1
    def _sift_down(self, location: int) -> None:
        while True:
            left = 2 * location + 1
            right =2 * location + 2
            if left >= len(self.heap):
                break
            smaller_child = left
            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smaller_child = right
            if self.heap[location] > self.heap[smaller_child]:
                self.heap[location], self.heap[smaller_child] = self.heap[smaller_child], self.heap[location]
                location = smaller_child
            else:
                break
                
            

        
        