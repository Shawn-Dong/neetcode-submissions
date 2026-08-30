class Node:
    def __init__(self, val=0):
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
        return self.size == 0 
        
    def appendleft(self, value: int) -> None:
        new = Node(value)
        front = self.head.next
        front.prev = new
        new.prev = self.head
        new.next = front
        self.head.next =new
        self.size +=1
        

    def append(self, value: int) -> None:
        new = Node(value)
        back = self.tail.prev
        new.prev = back
        back.next = new
        new.next = self.tail
        self.tail.prev = new
        self.size +=1

        
    def pop(self) -> int:
        if self.size == 0:
            return -1
        if self.size == 0:
            return -1
        back = self.tail.prev.prev 
        a = self.tail.prev.val
        back.next = self.tail
        self.tail.prev = back
        self.size -=1
        return a
        

    def popleft(self) -> int:
        if self.size == 0:
            return -1
        if self.size == 0:
            return -1
        front = self.head.next.next
        a = self.head.next.val
        self.head.next = front
        front.prev = self.head
        self.size -=1
        return a

        
