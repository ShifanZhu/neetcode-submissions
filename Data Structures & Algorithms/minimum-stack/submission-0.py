from collections import deque

class MinStack:

    def __init__(self):
        self._queue = deque()

    def push(self, val: int) -> None:
        self._queue.append(val)

    def pop(self) -> None:
        self._queue.pop()

    def top(self) -> int:
        return self._queue[-1]

    def getMin(self) -> int:
        return min(self._queue)
        
