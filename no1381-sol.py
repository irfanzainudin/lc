class CustomStack:
    # size = 0
    # stack = []

    # def __init__(self, maxSize: int):
    #     self.size = maxSize

    # def push(self, x: int) -> None:
    #     if len(self.stack) == self.size:
    #         return
    #     self.stack.append(x)

    # def pop(self) -> int:
    #     if len(self.stack) == 0:
    #         return -1
    #     return self.stack.pop()

    # def increment(self, k: int, val: int) -> None:
    #     if len(self.stack) < k:
    #         new_stack = []
    #         for s in self.stack:
    #             s += val
    #             new_stack.append(s)
    #         self.stack = new_stack
    #         return
    #     else:
    #         i = 0
    #         while (i < k):
    #             self.stack[i] += val
    #             i += 1

    def __init__(self, n: int):
        self.n, self.stack, self.inc = n, [], []

    def push(self, x: int) -> None:
        if len(self.stack) < self.n: self.stack.append(x), self.inc.append(0)

    def pop(self) -> int:
        if not self.stack: return -1
        if len(self.inc) > 1: self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if self.inc: self.inc[min(k, len(self.inc)) - 1] += val



# INPUTS:
# ["CustomStack","push","pop","increment","pop","increment","push","pop","push","increment","increment","increment"]
# [[2],[34],[],[8,100],[],[9,91],[63],[],[84],[10,93],[6,45],[10,4]]

# EXPECTED:
# [null,null,34,null,-1,null,null,63,null,null,null,null]

cs = CustomStack(2)
print(None)
print(cs.push(34))
print(cs.pop())
print(cs.increment(8, 100))
print(cs.pop())
print(cs.increment(9, 91))
print(cs.push(63))
print(cs.pop())
print(cs.push(84))
print(cs.increment(10, 93))
print(cs.increment(6, 45))
print(cs.increment(10, 4))