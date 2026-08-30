class Node:
    def __init__(self, val = 0):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def get(self, index:int) -> int:
        cur = self.head
        for i in range(index):
            if cur is None:
                return -1
            else:
                cur = cur.next
        return cur.value if cur else -1
    
    def remove(self, index:int) -> bool:
        if self.head is None:
            return False
        if index ==0: #删除第一个element
            self.head = self.head.next
            if self.head is None: #只有一个element的情况
                self.tail = None
            return True
        cur = self.head
        for i in range(index-1):
            if cur is None:
                return False
            cur = cur.next
        if cur is None or cur.next is None:
            return False
        pointer = cur.next.next
        if pointer is None:
            self.tail = cur
        cur.next = pointer
        return True

    def getValues(self) -> List[int]:
        res = []
        cur = self.head
        while cur:
            res.append(cur.value)
            cur = cur.next
        return res
        
