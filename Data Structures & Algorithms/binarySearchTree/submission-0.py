class TreeNode:
    def __init__(self,key :int , val:int):
        self.left = None
        self.key = key
        self.val =val
        self.right = None


class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        if self.root is None:
            self.root = TreeNode(key, val)
            return
        cur = self.root
        while True:
            if key < cur.key:
                if cur.left is None:
                    cur.left = TreeNode(key, val)
                    return
                cur = cur.left
            elif key > cur.key:
                if cur.right is None:
                    cur.right = TreeNode(key, val)
                    return
                cur = cur.right
            else:
                cur.val = val
                return

    def get(self, key: int) -> int:
        if self.root is None:
            return -1
        cur = self.root
        while True:
            if key < cur.key:
                if cur.left is None:
                    return -1
                cur = cur.left
            elif key > cur.key:
                if cur.right is None:
                    return -1
                cur = cur.right
            else:
                return cur.val
        return -1


    def getMin(self) -> int:
        if self.root is None:
            return -1
        cur = self.root
        while cur.left is not None:
            cur = cur.left
        res = cur.val
        return res

    def getMax(self) -> int:
        if self.root is None:
            return -1
        cur = self.root
        while cur.right is not None:
            cur = cur.right
        return cur.val

    def remove(self, key: int) -> None:
        def dfs(node, key):
            if node is None:
                return None
            if key < node.key:
                node.left = dfs(node.left, key)
            elif key > node.key:
                node.right = dfs(node.right, key)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                succ = node.right
                while succ.left:
                    succ = succ.left
                node.key, node.val = succ.key, succ.val
                node.right = dfs(node.right, succ.key)
            return node
        self.root = dfs(self.root, key)


    def getInorderKeys(self) -> List[int]:
        result = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            result.append(node.key)
            dfs(node.right)
        dfs(self.root)
        return result

