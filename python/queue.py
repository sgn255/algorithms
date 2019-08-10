# obj= Queue()
# obj.enqueue(x)
# obj.dequeue()
# param3 = obj.peek()
# bool = obj.isEmpty()


class Queue:

    def __init__(self):
        self.stack = []

    def enqueue(self, x):
        self.stack.append(x)

    def dequeue(self):
        if self.stack:
            self.stack = self.stack[1:]

    def peek(self):
        if self.stack:
            return self.stack[0]
        return None

    def isEmpty(self):
        if self.stack:
            return True
        return False
