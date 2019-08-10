# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# param_5 = obj.getMax()
# bool = obj.isEmpty()

class MinMaxStack:

    def __init__(self):
        self.stack = []
        self.min = None
        self.max = None

    def push(self, x):
        self.stack.append(x)

        if self.min is None or x < self.min :
            self.min = x

        if self.max is None or x > self.max:
            self.max = x

    def pop(self):
        if not self.stack:
            return

        pop= self.stack.pop()
        if  pop == self.mins:
            self.min = min(self.stack)
        elif pop == self.max:
            self.max = max(self.stack)

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.min not None:
            return self.min

    def getMax(self):
        if self.max not None:
            return self.min

    def isEmpty(self):
        if self.stack:
            return False
        return True
