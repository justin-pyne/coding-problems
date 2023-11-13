class MyQueue:

    def __init__(self):
        self.first = []
        self.second = []
        

    def push(self, x: int) -> None:
        self.first.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.second.pop()
        

    def peek(self) -> int:
        if len(self.second) == 0:
            for _ in range(len(self.first)):
                self.second.append(self.first.pop())
        return self.second[-1]
        

    def empty(self) -> bool:
        if len(self.first) == 0 and len(self.second) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()