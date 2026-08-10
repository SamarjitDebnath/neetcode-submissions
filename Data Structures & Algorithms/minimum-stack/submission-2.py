class MinStack:

    def __init__(self):
        self.stack = []
        # self.min_stack = []
        self._min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self._min = val
        else:
            self.stack.append(val - self._min)
            self._min = min(self._min, val)
        # self.min_stack.append(min((self.min_stack[-1] if self.min_stack else val), val))

    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        
        if pop < 0:
            self._min -= pop
        # self.min_stack.pop()

    def top(self) -> int:
        if self.stack[-1] >= 0:
            return self.stack[-1] + self._min
        return self._min
        # return self.stack[-1]

    def getMin(self) -> int:
        return self._min
        # return self.min_stack[-1]
        # return min(self.stack)
