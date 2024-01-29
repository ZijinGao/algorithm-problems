class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack2.append(x)

    def pop(self) -> int:
        self._move()
        ret = self.stack1.pop()
        return ret

    def peek(self) -> int:
        self._move()
        return self.stack1[-1]

    def empty(self) -> bool:
        return (not self.stack2) and (not self.stack1)
    
    def _move(self):
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())