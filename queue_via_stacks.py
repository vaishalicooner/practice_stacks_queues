# Implement a MyQueue class which implements a queue using two stacks.

class QueueViaStack():
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()


    def add(self,item):
        self.in_stack.push(item)

    def remove(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack):
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()