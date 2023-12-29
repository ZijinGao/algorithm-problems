from collections import deque
class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        if self.queue1:
            self.queue1.append(x)
        else:
            self.queue2.append(x)
        
    def pop(self) -> int:
        if self.queue1:
            while len(self.queue1)>1:
                self.queue2.append(self.queue1.popleft())
            return self.queue1.pop()
        else:
            while len(self.queue2)>1:
                self.queue1.append(self.queue2.popleft())
            return self.queue2.pop()

    def top(self) -> int:
        if self.queue1:
            return self.queue1[-1]
        else:
            return self.queue2[-1]

    def empty(self) -> bool:
        return not self.queue1 and not self.queue2