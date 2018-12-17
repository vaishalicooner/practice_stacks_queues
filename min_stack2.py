# How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element?

class min_stack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(Self,item):
        self.stack.append(item)
        if not self.min or item <= self.stack.min():
            self.min.append(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.stack_min():
            self.min.pop()
        return item

    def stack_min(self):
        return self.min[-1]

        