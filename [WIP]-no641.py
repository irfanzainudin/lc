class MyCircularDeque:
    size = 0
    q = []

    def __init__(self, k: int):
        self.size = k

    def insertFront(self, value: int) -> bool:
        if len(self.q) == self.size:
            return False
        else:
            self.q.insert(0, value)
            return True

    def insertLast(self, value: int) -> bool:
        if len(self.q) == self.size:
            return False
        else:
            self.q.append(value)
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.q.pop(0)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.q.pop()
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[len(self.q) - 1]

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.size


# Your MyCircularDeque object will be instantiated and called as such:
k = 3
value = 2

# Inputs:
# ["MyCircularDeque","insertFront","insertLast","insertFront","getRear","insertFront","getFront","getFront","insertFront","isFull","insertLast","getRear"]
# [[3],[2],[4],[6],[],[5],[],[],[6],[],[6],[]]
obj = MyCircularDeque(k)
print(obj.insertFront(value))
print(obj.insertLast(4))
print(obj.insertFront(value*3))
print(obj.getRear())
print(obj.insertFront(5))
print(obj.getFront())
print(obj.getFront())
print(obj.insertFront(6))
print(obj.isFull())
print(obj.insertLast(6))
print(obj.getRear())

# Expected:
# [null,true,true,true,4,false,6,6,false,true,false,4]