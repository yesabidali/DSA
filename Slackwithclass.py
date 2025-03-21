class Stack:
    def __init__(self):
        self.stack = []

    def show(self):
        return len(self.stack)

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0
    
s = Stack()
s.push(20)
s.push(30)
s.push(50)

print("Stack size:", s.show())
print("Top element:", s.peek())
print("Popped element:", s.pop())
print("Stack after pop:", s.stack)
