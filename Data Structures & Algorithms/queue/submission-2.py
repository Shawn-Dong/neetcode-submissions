class Node:
    def __init__(self, val = 0):
        self.val = val
        self.prev = None
        self.next = None



class Deque:
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def append(self, value: int) -> None:
        node = Node(value)
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node
        self.size += 1
        

    def appendleft(self, value: int) -> None:
        node = Node(value)
        first = self.head.next
        first.prev = node
        node.next = first
        self.head.next = node
        node.prev = self.head
        self.size += 1
        

    def pop(self) -> int:
        if self.size == 0:
            return -1
        last = self.tail.prev
        last.prev.next = self.tail
        self.tail.prev = last.prev
        self.size -= 1
        return last.val
        

    def popleft(self) -> int:
        if self.size == 0:
            return -1
        first = self.head.next
        firstval = first.val
        first.next.prev = self.head
        self.head.next = first.next
        self.size -=1
        return firstval

        
