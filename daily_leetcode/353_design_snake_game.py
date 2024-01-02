from collections import deque
class SnakeGame:
    def __init__(self, width: int, height: int, food: list[list[int]]):
        self.width = width
        self.height = height
        self.snake = deque([(0,0)])
        self.snakeset = {(0,0)} # reduce the time complexity for looking for ceil in snake to be O(1)
        self.food = food
        self.foodidx = 0 # the index of the upcoming food 
        self.movement = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}

    def move(self, direction: str) -> int:
        newHead = (self.snake[0][0] + self.movement[direction][0],
                   self.snake[0][1] + self.movement[direction][1])

        crosses_boundary1 = newHead[0] < 0 or newHead[0] >= self.height
        crosses_boundary2 = newHead[1] < 0 or newHead[1] >= self.width
        bites_itself = newHead in self.snakeset and newHead != self.snake[-1]
        if crosses_boundary1 or crosses_boundary2 or bites_itself:
            return -1

        next_food_item = self.food[self.foodidx] if self.foodidx < len(self.food) else None
        if self.foodidx < len(self.food) and next_food_item[0] == newHead[0] and next_food_item[1] == newHead[1]:
            self.foodidx += 1
        else:
            tail = self.snake.pop()
            self.snakeset.remove(tail)

        self.snake.appendleft(newHead)
        self.snakeset.add(newHead)
        return len(self.snake)-1
